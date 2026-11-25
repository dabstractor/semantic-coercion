"""Standalone runner for Semantic Coercion (SC) evaluation scenarios (v0).

Calls the NVIDIA NIM OpenAI-compatible endpoint directly with ``requests``.
No pi-extension dependency: this module is importable on its own.

Usage:
    from sc.runner import run_scenario

    result = run_scenario("s01", instruction="Make the minimal edit ...")
    print(result.text, result.input_tokens, result.output_tokens, result.latency_ms)

CLI:
    python -m sc.runner --scenario-id s01 [--instruction "..."] \
        [--system-prompt "..."] [--temperature 0.0] [--max-tokens 1024]
"""

from __future__ import annotations

import argparse
import json
import os
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import requests
import yaml

BASE_URL = "https://integrate.api.nvidia.com/v1"
DEFAULT_MODEL = "nvidia/nemotron-3.5-lightning-30b-a3b"
API_KEY_ENV_VAR = "NVIDIA_NIM_API_KEY"
RATE_LIMIT_BACKOFF_SECONDS = 60.0
DEFAULT_TIMEOUT_SECONDS = 120.0
DEFAULT_MAX_RATE_LIMIT_RETRIES = 3
DEFAULT_MAX_TOKENS = 1024
SCENARIOS_PATH = Path(__file__).resolve().with_name("scenarios.yaml")

REQUIRED_SCENARIO_FIELDS = (
    "id",
    "name",
    "setup",
    "directive_under_test",
    "evaluation_focus",
    "failure_modes_to_detect",
)


class RunnerError(RuntimeError):
    """Base error for the SC runner."""


class MissingAPIKeyError(RunnerError):
    """Raised when NVIDIA_NIM_API_KEY is not set and no key was passed."""


class RateLimitExceededError(RunnerError):
    """Raised when the endpoint keeps returning 429 after all backoff retries."""


class ModelEndOfLifeError(RunnerError):
    """Raised when the endpoint returns 410 (model end-of-life); not retried."""


@dataclass
class ScenarioResult:
    """Outcome of one scenario run against the NIM endpoint."""

    text: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    raw_response: dict[str, Any]
    scenario_id: str = ""
    model: str = ""
    instruction: str = ""

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_scenarios(path: str | Path = SCENARIOS_PATH) -> list[dict[str, Any]]:
    """Load and validate the seed scenarios from ``scenarios.yaml``."""
    path = Path(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    scenarios = (data or {}).get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError(f"No scenarios found in {path}")
    for scenario in scenarios:
        missing = [f for f in REQUIRED_SCENARIO_FIELDS if f not in scenario]
        if missing:
            raise ValueError(
                f"Scenario {scenario.get('id', '<unknown>')!r} in {path} "
                f"is missing required fields: {missing}"
            )
    return scenarios


def get_scenario(
    scenario_id: str, path: str | Path = SCENARIOS_PATH
) -> dict[str, Any]:
    """Return the scenario with the given id, or raise KeyError."""
    for scenario in load_scenarios(path):
        if scenario["id"] == scenario_id:
            return scenario
    available = [s["id"] for s in load_scenarios(path)]
    raise KeyError(
        f"Unknown scenario_id {scenario_id!r}; available: {available}"
    )


def _resolve_api_key(api_key: str | None) -> str:
    key = api_key or os.environ.get(API_KEY_ENV_VAR)
    if not key:
        raise MissingAPIKeyError(
            f"Set the {API_KEY_ENV_VAR} environment variable or pass api_key=..."
        )
    return key


def _build_messages(
    scenario: dict[str, Any] | None,
    instruction: str,
    system_prompt: str | None,
) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    user_parts: list[str] = []
    if scenario is not None:
        user_parts.append(f"Scenario: {scenario['name']}\n\nSetup:\n{scenario['setup']}")
    user_parts.append(f"Instruction under test:\n{instruction}")
    messages.append({"role": "user", "content": "\n\n".join(user_parts)})
    return messages


def _post_with_retries(
    url: str,
    headers: dict[str, str],
    payload: dict[str, Any],
    *,
    timeout: float,
    max_rate_limit_retries: int,
    backoff_seconds: float,
) -> tuple[dict[str, Any], float]:
    """POST to the chat-completions endpoint; returns (json_body, latency_ms).

    429 responses are retried with ``backoff_seconds`` (default 60s) between
    attempts, up to ``max_rate_limit_retries`` retries. 410 (model EOL) raises
    ModelEndOfLifeError immediately without retrying.
    """
    retries_used = 0
    start = time.perf_counter()
    while True:
        try:
            response = requests.post(
                url, headers=headers, json=payload, timeout=timeout
            )
        except requests.RequestException as exc:
            raise RunnerError(f"Request to {url} failed: {exc}") from exc

        if response.status_code == 200:
            latency_ms = (time.perf_counter() - start) * 1000.0
            return response.json(), latency_ms

        body_snippet = response.text[:500]
        if response.status_code == 429:
            if retries_used >= max_rate_limit_retries:
                raise RateLimitExceededError(
                    f"HTTP 429 rate limit persisted after {retries_used} "
                    f"retries with {backoff_seconds}s backoff from {url}: "
                    f"{body_snippet}"
                )
            retries_used += 1
            time.sleep(backoff_seconds)
            continue

        if response.status_code == 410:
            raise ModelEndOfLifeError(
                f"HTTP 410 from {url}: the requested model is end-of-life. "
                f"Choose a different model (current: {payload.get('model')!r}). "
                f"Body: {body_snippet}"
            )

        raise RunnerError(
            f"HTTP {response.status_code} from {url}: {body_snippet}"
        )


def run_scenario(
    scenario_id: str,
    instruction: str | None = None,
    system_prompt: str | None = None,
    temperature: float = 0.0,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    *,
    model: str = DEFAULT_MODEL,
    base_url: str = BASE_URL,
    api_key: str | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_rate_limit_retries: int = DEFAULT_MAX_RATE_LIMIT_RETRIES,
    backoff_seconds: float = RATE_LIMIT_BACKOFF_SECONDS,
    scenarios_path: str | Path = SCENARIOS_PATH,
) -> ScenarioResult:
    """Run one SC scenario against the NIM OpenAI-compatible endpoint.

    Args:
        scenario_id: Id of a scenario in ``scenarios.yaml`` (e.g. ``"s01"``).
            Used to look up the scenario setup; if the id is unknown, the
            scenario block is omitted from the prompt.
        instruction: The directive under test. If None, the scenario's own
            ``directive_under_test`` from ``scenarios.yaml`` is used.
        system_prompt: Optional system message placed before the user turn.
        temperature: Sampling temperature.
        max_tokens: Max completion tokens.
        model: NIM model name (default: DEFAULT_MODEL).
        base_url: OpenAI-compatible base URL (default: NIM integrate API).
        api_key: API key; falls back to the NVIDIA_NIM_API_KEY env var
            (required if not passed).
        timeout: Per-request timeout in seconds.
        max_rate_limit_retries: Number of 429 retries before giving up.
        backoff_seconds: Sleep between 429 retries (default 60s).
        scenarios_path: Path to scenarios.yaml.

    Returns:
        ScenarioResult with response text, input_tokens, output_tokens,
        latency_ms, and the raw JSON response.

    Raises:
        MissingAPIKeyError: if no API key is available.
        ModelEndOfLifeError: on HTTP 410 (model EOL).
        RateLimitExceededError: on persistent HTTP 429.
        RunnerError: on other request/HTTP/parse failures.
    """
    key = _resolve_api_key(api_key)

    scenario: dict[str, Any] | None = None
    for candidate in load_scenarios(scenarios_path):
        if candidate["id"] == scenario_id:
            scenario = candidate
            break

    if instruction is None:
        if scenario is None:
            raise ValueError(
                f"instruction is required: scenario_id {scenario_id!r} was not "
                f"found in {scenarios_path}"
            )
        instruction = scenario["directive_under_test"]

    messages = _build_messages(scenario, instruction, system_prompt)
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    url = f"{base_url.rstrip('/')}/chat/completions"

    raw_response, latency_ms = _post_with_retries(
        url,
        headers,
        payload,
        timeout=timeout,
        max_rate_limit_retries=max_rate_limit_retries,
        backoff_seconds=backoff_seconds,
    )

    try:
        choice = raw_response["choices"][0]
        text = choice["message"].get("content") or ""
        usage = raw_response.get("usage") or {}
        input_tokens = int(usage.get("prompt_tokens", 0))
        output_tokens = int(usage.get("completion_tokens", 0))
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise RunnerError(
            f"Malformed response from {url}: {exc}; raw_response={raw_response!r}"
        ) from exc

    return ScenarioResult(
        text=text,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_ms=round(latency_ms, 3),
        raw_response=raw_response,
        scenario_id=scenario_id,
        model=model,
        instruction=instruction,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run an SC evaluation scenario against the NIM endpoint."
    )
    parser.add_argument("--scenario-id", required=True, help="e.g. s01")
    parser.add_argument(
        "--instruction",
        default=None,
        help="Directive under test (default: the scenario's directive_under_test)",
    )
    parser.add_argument("--system-prompt", default=None)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-url", default=BASE_URL)
    args = parser.parse_args(argv)

    result = run_scenario(
        args.scenario_id,
        instruction=args.instruction,
        system_prompt=args.system_prompt,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        model=args.model,
        base_url=args.base_url,
    )
    print(json.dumps(result.as_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
