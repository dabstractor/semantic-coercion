"""Semantic Coercion (SC) evaluation framework v0.

Seed behavioral scenarios (PRD §4 S4) plus a standalone runner for the
NVIDIA NIM OpenAI-compatible endpoint.
"""

from .runner import (
    API_KEY_ENV_VAR,
    BASE_URL,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    RATE_LIMIT_BACKOFF_SECONDS,
    SCENARIOS_PATH,
    MissingAPIKeyError,
    ModelEndOfLifeError,
    RateLimitExceededError,
    RunnerError,
    ScenarioResult,
    get_scenario,
    load_scenarios,
    run_scenario,
)

__version__ = "0.1.0"

__all__ = [
    "API_KEY_ENV_VAR",
    "BASE_URL",
    "DEFAULT_MAX_TOKENS",
    "DEFAULT_MODEL",
    "RATE_LIMIT_BACKOFF_SECONDS",
    "SCENARIOS_PATH",
    "MissingAPIKeyError",
    "ModelEndOfLifeError",
    "RateLimitExceededError",
    "RunnerError",
    "ScenarioResult",
    "get_scenario",
    "load_scenarios",
    "run_scenario",
]
