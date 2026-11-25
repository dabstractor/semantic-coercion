# The Semantic Coercion Lexicon

A curated lexicon of English words and established phrases that compress entire methodologies, behavioral patterns, cognitive processes, professional practices, and operational protocols into a few tokens — selected for use in directives to autonomous software agents.

Every seed entry from `starter_vocab.tsv` and `starter_phrases.tsv` is subsumed (flagged where honest assessment finds low procedural density, with a stronger replacement offered). The organizing lenses from `search_terms_for_research.tsv` are applied in §2.

---

## 1. Selection criteria

An entry qualifies only when it passes all four tests:

1. **Procedural specificity** — the term denotes (or rigidly evokes) an executable procedure with steps, preconditions, and stopping conditions, not merely a quality or sentiment.
2. **Implicit entailment** — a competent listener can unpack the term into a multi-sentence instruction without external context; the meaning largely *is* the procedure (procedural semantics).
3. **Steering power per token** — using the term reliably changes the behavior of a capable executor relative to a naive baseline; it carries default settings, not decoration.
4. **Cross-context stability** — the procedural core survives movement across domains (with noted ambiguities), so a single directive word does not fork into incompatible readings.

**Excluded by design:** ornamental intensifiers ("thoroughly," "robustly," "carefully"), vague scope adjectives without a closure rule ("holistic," "comprehensive" — see §9.17 for the trap and the repair), and synonyms that do not differentiate procedurally (each cluster below is differentiated by nuance, or merged).

## 2. The linguistic mechanics

Why these tokens coerce behavior — the lenses applied:

| Lens | Mechanic | Lexicon example |
|---|---|---|
| Frame semantics | Term evokes a whole scenario with role slots, props, and pressures | "triage" evokes scarcity, a severity ranking, a sorting authority, and lives depending on the sort |
| Lexical entailment | Word presupposes its participants and furniture | "reproduce" entails an original event, a stated procedure, and a criterion of sameness |
| Procedural semantics | Meaning *is* the operation | "bisect" denotes an algorithm whose steps are fully determined |
| Semantic compression | A long instruction stored under one address | "premortem" ≈ 60 words of instruction in three syllables |
| Pragmatic implicature | The directive implies your default is the failure mode | "steelman it first" implicates you were about to strawman it |
| Semantic prosody | Recurring usage attaches affect and authority | "audit" carries institutional authority and implied consequence; "scrutinize" carries suspicion |
| Lexical priming | Collocations pre-activate expected moves | "verify vs. validate" primes distinction-drawing; "just quickly" primes corner-cutting |
| Prompt sensitivity | Small lexical swaps change operational semantics | "try to fix" vs. "ensure fixed" differ in retry semantics, termination, and escalation duty |

## 3. Deployment guidance

1. **Run the expansion test.** A dense term is only as good as the agent's expansion of it. Before relying on a term, ask the agent to expand it into procedure; audit and correct the expansion once, then trust the address.
2. **Prefer phrases over adjectives when precision is load-bearing.** "Fail closed" beats "be safe"; "exception-only reporting" beats "be concise."
3. **Compound carefully.** Terms compose into operating stances: "premortem → define abort criteria → report exception-only" is a complete control loop in nine tokens. But compounding rare terms ("run an ACH, hold a WARNO, FRAGO the delta") assumes shared background — gloss on first use.
4. **Respect polysemy traps.** Terms whose senses fork across domains (below) need a one-word disambiguator in the directive.
5. **Density decays with rarity.** Small models may return nothing for "estimative language" or "ACH"; include a parenthetical gloss or fall back to the expanded instruction.

**Polysemy traps** (term · competing senses · repair):

| Term | Forking senses | Repair |
|---|---|---|
| ground | electrical · NLP grounding · evidence-basis · mutual understanding (Clark) | "ground the claim in logs" |
| canary | canary release · canary token/trap · sentinel bird | "canary-release to 1%," "canary token on the path" |
| sentinel | sentinel metric · sentinel value (-1/null) | "sentinel metric: errors per minute" |
| pin | version pinning · blame-pinning · hardware interrupt | "pin the digest in the lockfile" |
| spike | timeboxed exploration · traffic spike · spike solution | "run a two-day spike on the parser" |
| drift | config drift · model/data drift · slow steering drift | "detect schema drift vs. declared state" |
| audit | log audit · compliance audit · code audit · access review | "audit the changes against policy X" |
| quarantine | malware isolation · exposure isolation · DLQ parking | "quarantine the message, not the queue" |
| sandbox | dev playground · security containment · test status | "run sandboxed: no net, tmpfs only" |
| validate | spec-conformance · meets-need · input well-formedness | say "verify against spec" or "validate input shape" |
| normalize | canonicalize data · statist. normalization · normalize deviance | "normalize keys to snake_case" |
| instrument | add telemetry · measuring device · legal document | "instrument the handler with a timer" |
| escalate | raise severity · raise to a human · increase a parameter | "escalate to on-call at severity 2" |
| provision | grant resources · legal proviso | "provision the staging namespace" |

**Anti-lexicon** — strip these from directives; they carry affect without procedure, and often license the opposite of intent:

- "just," "simply," "obviously," "clearly" — minimize perceived effort and suppress scrutiny.
- "carefully," "thoroughly," "rigorously," "robustly" — intensity without a checkable criterion.
- "holistic," "comprehensive," "end-to-end" (unqualified) — scope inflation without a closure rule.
- "best practices" — defers the actual standard; name the standard.
- "state-of-the-art," "cutting-edge" — provenance-free quality claim.
- "as needed," "where appropriate" — silently delegates the hard decision back to the executor's mood.
- "try" (unqualified) — pre-authorizes giving up without a retry count or escalation condition.

---

# The Lexicon

## 1. Epistemics & Evidential Standards
*Source fields: epistemology, law of evidence, intelligence analysis, science.*

### Falsify
- **Implied procedure:** Design tests that could prove the claim wrong; run the strongest such test first; treat survival as the only evidence in favor; discard the claim on first clean disconfirmation.
- **Replaces:** Don't look for confirming evidence. Construct the scenario most likely to expose the hypothesis as false, execute it, and abandon the hypothesis if it fails there.
- **Ambiguity:** Collides with the fraud sense ("falsified data" = fabricated); in stats, "falsifiable" is a property of claims, not an action you perform.
- **Directive:** Before merging, falsify the fix: write the one test most likely to resurface the race, run it on the repro branch, and revert if it fails.

### Corroborate
- **Implied procedure:** For each load-bearing claim, obtain confirmation from a second source or method; argue why the second source does not share the first's failure mode; withhold belief until the second witness arrives.
- **Replaces:** Find independent confirmation before treating this as fact; two echoes of the same upstream error don't count — verify the sources are actually independent.
- **Ambiguity:** "Substantiate" (supply support for a specific claim) is its near-twin; corroborate stresses the second independent witness, substantiate stresses bringing the supporting evidence at all.
- **Directive:** Corroborate the outage window against both the LB access logs and the client-side error beacon before writing the postmortem timeline.

### Independent corroboration
- **Implied procedure:** Enumerate the candidate witnesses; for each, trace its causal origin; accept only witnesses whose evidence-generating process is disjoint from the primary claim's; document the independence argument.
- **Replaces:** Confirm this through a channel that could not have been contaminated by the same error — a different instrument, a different team, a different physical path.
- **Ambiguity:** "Independent" is asserted far more often than argued; copy-paste, syndication, and shared upstreams silently destroy it.
- **Directive:** The vendor says the API is healthy — get independent corroboration from our own synthetic probe before closing the ticket.

### Substantiate
- **Implied procedure:** Attach the specific supporting artifact (measurement, citation, log line) to the exact claim it supports; unsupported claims are downgraded to speculation or retracted.
- **Replaces:** Back each assertion with its evidence in the same breath; if you cannot point to where a claim came from, mark it as a guess.
- **Ambiguity:** Weaker than corroborate (no second-source demand); management-speak ("substantiate your estimate") can drain it to ceremony.
- **Directive:** Substantiate every number in the exec summary with a link to the query that produced it.

### Triangulate
- **Implied procedure:** Derive the answer by at least two methodologically distinct routes; if the routes agree within tolerance, commit; if they diverge, the divergence itself is the finding — investigate before choosing.
- **Replaces:** Estimate this several independent ways — different data, different instruments, different models — and only trust the answer where the approaches converge; treat disagreement as a lead, not noise.
- **Ambiguity:** Navigation heritage misread as "exactly three sources" or as mere "gather more data"; the load-bearing element is method diversity, not count.
- **Directive:** Triangulate the leak: heap profile delta, allocator stats, and a load-repro — reconcile all three estimates or flag the conflict.

### Ground truth
- **Implied procedure:** Identify the most authoritative measurable form of the quantity of interest; evaluate against it directly, never against proxies or predecessors; when the true value is unobservable, state which proxy substitutes and its known skew.
- **Replaces:** Score your output against reality itself — verified samples, production behavior, the actual users — not against the old system's output or your own expectation.
- **Ambiguity:** In ML it means the labeled reference set specifically; colloquially any "authoritative" source — and authority is often inherited, not real.
- **Directive:** We need ground truth before tuning: hand-verify 200 extractions; the old parser's output is not ground truth.

### Burden of proof
- **Implied procedure:** Assign default ownership of evidence duty to the claimant; scale the required evidence to the claim's extraordinariness and blast radius; unmet burden means the claim is not acted on, not that it is false.
- **Replaces:** Whoever asserts this carries the obligation to support it — the bigger the consequence if wrong, the more evidence required — and until it arrives we proceed as if unconvinced.
- **Ambiguity:** Who holds it must be stated or fights erupt; reversing it ("prove it's NOT broken") is a standard rhetorical hijack to flag.
- **Directive:** "The config can't be the cause" is an assertion: the burden of proof is on us, so instrument the config path before ruling it out.

### Due diligence
- **Implied procedure:** Before commitment, run an independent verification pass proportionate to the stakes: re-derive the counterparty's claims from primary artifacts, enumerate known failure modes of this class of deal, and record findings as go/no-go evidence.
- **Replaces:** Do not take their word or your first impression: independently check the claims, inspect the artifacts, look for the standard traps in this kind of transaction, and document what you verified before you commit.
- **Ambiguity:** Legal sense is transaction-specific with defined checklists; casual use drains to "we looked at it"; specify which checklist.
- **Directive:** Run due diligence on the dependency: read the repo, check the CVE feed, confirm the license, test the failure path — then decide on adoption.

### Defeasible
- **Implied procedure:** Hold the conclusion with an explicit overturn condition: name the observation that would reverse it, keep reversal cheap, and re-open the case immediately when the trigger fires.
- **Replaces:** This conclusion stands only until contrary evidence appears — state now what would change it, and structure the work so changing course later is cheap.
- **Ambiguity:** Reads as "tentative/weak" (low confidence) though it is a structural property (overturnable by named evidence at any confidence level); distinguish from provisional.
- **Directive:** Mark the CPU-theory attribution defeasible: we act on it, and any core dump showing idle threads reopens the investigation.

### Prima facie
- **Implied procedure:** Accept the case as valid on its face for immediate action, while scheduling the challenge pass; explicit that first appearance, not full proof, is the current warrant.
- **Replaces:** On first inspection this holds, so proceed — but only until someone stress-tests the appearance, and expect the challenge to come.
- **Ambiguity:** Legal threshold of "rebuttable presumption" vs. casual "at first glance"; also read as mere hedging by those skipping the challenge step.
- **Directive:** Prima facie the migration caused the spike — roll it back now, and schedule the falsification pass before we blame it permanently.

### Estimative language
- **Implied procedure:** Attach a calibrated probability band to every judgment, drawn from a defined scale (e.g., "high confidence ≈ 80–95%"), tied to named evidence, with the diagnostic that would move the band.
- **Replaces:** Say how sure you are using a fixed numeric or ordinal scale everyone interprets the same way, and say what evidence would make you more or less sure.
- **Ambiguity:** Verbal probabilities ("likely") map inconsistently across readers (60%? 90%?); the scale must be pinned in the prompt. Intelligence-community standard (ICD 203) is the reference implementation.
- **Directive:** All findings get estimative language: "high confidence (≈85%) thermal throttling; low confidence on the driver theory — the fan telemetry would settle it."

### Observation–inference–assumption separation
- **Implied procedure:** Tag every statement in the record with its epistemic type — directly observed (with instrument), inferred (with rule), or assumed (with no current evidence); never let an assumption migrate into the observed column without a new measurement.
- **Replaces:** Sort everything you know into three lists: what you actually saw, what you concluded from it, and what you're taking on faith — and keep the three visibly separate as work proceeds.
- **Ambiguity:** Boundaries blur on interpreted tool output (a parser's AST is observed data about the parse, inferred about the program); state the tagging rule once.
- **Directive:** Incident notes use three sections — OBSERVED / INFERRED / ASSUMED — and nothing moves up a section without a cited measurement.

### Null-result discipline
- **Implied procedure:** Record every search that found nothing, with its scope and method; distinguish "absence of evidence" (didn't look there) from "evidence of absence" (looked thoroughly, not present); propagate the distinction to conclusions.
- **Replaces:** Report what you looked for and failed to find, and where you looked — "not found in the places I checked" is different from "doesn't exist," and conclusions must respect that difference.
- **Ambiguity:** Reads as defeatism in status-report culture; requires the reporter to specify search scope, which the lazy will omit.
- **Directive:** Log null results explicitly: "no matching LDAP entry — searched OUs X and Y with filter Z," so nobody mistakes un-searched space for empty space.

### Provenance
- **Implied procedure:** For every artifact and datum, record origin, custody history, and transformations applied; make the record tamper-evident; treat any artifact whose chain is broken as untrusted for consequential decisions.
- **Replaces:** Track where this came from, who touched it, and what changed at each step — and if that history can't be reconstructed, don't base decisions on it.
- **Ambiguity:** Art-history origin sense vs. supply-chain (SLSA) attestation sense vs. data lineage; specify which ledger.
- **Directive:** Attach provenance to each figure in the report: source file, commit, extraction query, and transform script.

### Chain of custody
- **Implied procedure:** Every transfer of the artifact between handlers is logged (who, when, hash); integrity is verified at each hop; any gap voids the artifact's evidentiary standing, whatever its content.
- **Replaces:** From collection to presentation, this evidence must never be in an unlogged state — log every handoff, checksum at every step, and if there's a gap, the evidence is inadmissible even if it looks fine.
- **Ambiguity:** Forensic/legal origin; overkill for casual logs but exactly right for security incidents, evaluation datasets, and audit artifacts; not the same as mere "versioning."
- **Directive:** Maintain chain of custody on the captured VM image: sha256 at acquisition, logged at each analyst transfer, hashes re-verified before it's cited in the finding.

### Ascertain
- **Implied procedure:** Establish the fact by direct inquiry at the authoritative source before relying on it; the word asserts that certainty was achieved by investigation, not assumption.
- **Replaces:** Go find out for certain — check the source itself, don't inherit someone's belief — and only then treat the matter as settled.
- **Ambiguity:** **Low procedural density** (this lexicon's honest flag): denotes the achieved state more than the method; pair it with the method ("ascertain by querying the schema registry") or it decorates.
- **Directive:** Ascertain the actual retention setting by querying the bucket policy — don't infer it from the console screenshot.

### Scrutinize
- **Implied procedure:** Examine item by item with an adversarial posture: for each element, ask how it could be wrong, incomplete, or deceptive; nothing passes by appearance.
- **Replaces:** Examine this as if it were prepared by someone trying to slip something past you — check each claim's basis, each number's derivation, each step's edge cases.
- **Ambiguity:** Semantic prosody of suspicion (assumes a possibly-untrustworthy object); weaker siblings "review" and "examine" lack the hostility; "scrutiny" without a checklist often decays to skimming.
- **Directive:** Scrutinize the diff for the failure modes on our list: error swallowing, lockscope, and silent truncation — one pass per failure mode.

### Audit
- **Implied procedure:** Systematically examine the whole population against a named standard, by an examiner independent of the author, producing findings classified by severity and traceable to evidence.
- **Replaces:** Check every item, not a sample, against this specific written standard, from outside the team that made it, and produce a severity-ranked report where each finding cites its evidence.
- **Ambiguity:** Forks into log-audit, compliance-audit, code-audit, access-review; each has a different population and standard — name both. Independence is the often-dropped load-bearing wall.
- **Directive:** Audit all 214 endpoints against the auth matrix: independent reviewer, severity per finding, evidence link per row.

## 2. Reasoning Operations
*Source fields: logic, mathematics, engineering habits, decision theory.*

### First-principles reasoning
- **Implied procedure:** Reduce the problem to verified fundamentals (physical laws, measured constants, stated constraints); rebuild the answer upward from them; discard analogies and inherited defaults mid-derivation.
- **Replaces:** Don't reason from how others do it or how we did it before — decompose to the facts you can verify at the bottom, and construct the answer from those facts alone.
- **Ambiguity:** Sloganized in startup culture into "ignore precedent," which is not licensed; precedent remains evidence, just not proof. Expensive at full rigor — reserve for load-bearing questions.
- **Directive:** First-principles the storage bill: bytes × replication × region price × egress; compare to the invoice before accepting any optimization narrative.

### Deduce / induce / abduce (inference-mode selector)
- **Implied procedure:** Declare which mode is in use: deduce (derive what must follow from accepted premises), induce (generalize from enumerated instances, with sample stated), abduce (propose the best explanation of observations, with testability attached); do not silently switch modes mid-argument.
- **Replaces:** Say whether you're deriving, generalizing, or explaining — the warrant, the failure mode, and the required check differ for each, and arguments fail when they drift between modes.
- **Ambiguity:** "Infer" covers all three (umbrella term); "deduce" is colloquially misused for any reasoning; abduction licenses storytelling unless a discriminating test is attached.
- **Directive:** Label each step in the RCA: deduced from the invariant, induced from 3 instances, or abduced pending the trace.

### Extrapolate
- **Implied procedure:** Project beyond the observed range only with an explicit model, stated confidence decay with distance, and a boundary beyond which the projection is void.
- **Replaces:** Extending the trend past your data is allowed, but name the model you're trusting, admit the uncertainty grows with distance, and declare the point where the answer becomes meaningless.
- **Ambiguity:** Interpolation (inside the range) quietly masquerades as extrapolation (outside it); trend-line culture treats it as free — it is the most failure-prone move in forecasting.
- **Directive:** Extrapolate load to Q3 with a stated model and halved confidence per quarter; void the estimate past two quarters out.

### Synthesize
- **Implied procedure:** Combine multiple sources into a construction that is more than any source contains: resolve their conflicts, preserve their constraints, and produce an integrated artifact with a stated resolution policy for disagreements.
- **Replaces:** Don't summarize each document in turn — merge them into one coherent answer, say where they conflict, and say how you resolved each conflict.
- **Ambiguity:** Downgraded to "summarize" in casual use; synthesis without a conflict-resolution policy produces hidden cherry-picking.
- **Directive:** Synthesize the three design docs into one spec; every disagreement gets a resolution line citing which constraint won.

### Reconcile
- **Implied procedure:** Place the conflicting records side by side; identify the exact field-level discrepancies; resolve each by tracing to authority or timing; if irreconcilable, quarantine the difference as a documented open item.
- **Replaces:** Make these two accounts agree — find each spot where they differ, determine which is right and why, and explicitly list anything you couldn't settle.
- **Ambiguity:** Accounting origin (reconcile the ledger) vs. interpersonal ("reconcile with Bob"); the operative act is forced agreement or documented impasse, not averaging — averaging is the classic malpractice.
- **Directive:** Reconcile the inventory DB against the deploy manifests; any drift you can't explain gets an open item, not a silent overwrite.

### Parsimony, with Hickam's counterweight
- **Implied procedure:** Prefer the explanation with the fewest unverified moving parts; but when the evidence shows multiple simultaneous causes, do not force one — a single-cause conclusion must beat the multi-cause account on evidence, not elegance.
- **Replaces:** Choose the simplest story that fits, unless the data actually indicates several things went wrong at once — Occam is a tiebreaker between equally supported rivals, not a club to beat complexity down with.
- **Ambiguity:** "Occam's razor" misread as "simplest is true"; Hickam's dictum ("patients can have as many diseases as they please") is the clinical counterweight; in incident analysis, multi-cause is the norm, not the exception.
- **Directive:** Apply parsimony with the Hickam check: prefer the single-cause story only if it explains all symptoms; otherwise model the concurrent faults.

### Decompose
- **Implied procedure:** Partition the problem into subproblems chosen so that each is independently verifiable and their interfaces are explicit; assign each part a completion test; the partition is wrong if parts cannot be checked in isolation.
- **Replaces:** Break this into pieces you can each test on their own, define exactly what passes between the pieces, and know how you'd verify each piece separately before you build.
- **Ambiguity:** Decomposition along organizational seams rather than verification seams produces parts that can't be independently checked — the criterion is testability, not team structure.
- **Directive:** Decompose the migration into extract, dual-write, verify, cutover — each with its own pass/fail probe before we start any of them.

### Bisect
- **Implied procedure:** Maintain an interval known to contain the transition; test the midpoint; discard the half the test excludes; repeat until the interval is a single step; log every probe.
- **Replaces:** Find the exact change by halving: test the middle commit, throw away the half that's clean, and keep halving until one commit remains — never scan linearly.
- **Ambiguity:** Requires a reliable oracle test and a monotone history; merge-conflicted or behavior-dependent breakage defeats it — say so and switch strategies rather than force it.
- **Directive:** Bisect the regression from v1.8 to HEAD using the flake-suite as oracle; report the commit and the probe log.

### Invert, always invert
- **Implied procedure:** Solve backward from the failure or the end state: enumerate what would guarantee the bad outcome, then design to prevent exactly those; ask "what would make this inevitably fail" before "how do we succeed."
- **Replaces:** Instead of listing success factors, list everything that would certainly sink this and eliminate those first — avoiding stupidity beats seeking brilliance.
- **Ambiguity:** Mathematical inversion (invert the matrix) collides rhetorically; the via negativa (define by exclusion) is its epistemic cousin; not a full substitute for forward planning — a paired move.
- **Directive:** Invert the launch: write the five ways this launch certainly dies (quota, cold cache, lock contention, rollback gap, comms gap) and close those five first.

### Fermi estimate
- **Implied procedure:** Decompose the quantity into factors you can bound from knowledge; estimate each within an order of magnitude; multiply; treat the result as a sanity envelope, not a prediction.
- **Replaces:** Get a rough number now by breaking it into factors you can guesstimate — it only needs to be right within 10×, and it needs to exist before anyone argues from vibes.
- **Ambiguity:** Anachronistic precision (three significant figures) defeats the purpose; the deliverable is the envelope and the factor list, not the point value.
- **Directive:** Fermi the egress cost: users × page weight × retry rate × $/GB — if it clears $1k/day, we profile before we ship.

### Necessary vs. sufficient
- **Implied procedure:** Classify each proposed condition as necessary (without it, no outcome), sufficient (with it, outcome follows), or both; check arguments for the silent swap of one for the other; repair by restating with "only if" / "if."
- **Replaces:** For every condition, say whether it's required, or enough, or both — most bad arguments here quietly treat a requirement as a guarantee.
- **Ambiguity:** English "if" casually means all four of if/only-if/if-and-only-if/unless; natural-language specs inherit the ambiguity wholesale.
- **Directive:** Label each precondition in the runbook N or S or N+S — and flag anywhere the text says "if" where the behavior needs "only if."

### But-for counterfactual test
- **Implied procedure:** For each candidate cause, ask whether the outcome would have occurred without it, holding the rest fixed; causes that fail the test are demoted to context; verify the final cause by mentally removing it and observing the imagined outcome change.
- **Replaces:** Before naming something the cause, subtract it in your head and see if the failure still happens — if the failure survives the subtraction, you've found a contributor, not the cause.
- **Ambiguity:** Legal proximate-cause doctrine layers policy limits (foreseeability) on top of the bare counterfactual; over-selects in conjunctive causation (every necessary condition passes).
- **Directive:** Run but-for on each candidate: remove the config push — outage persists; remove the pool exhaustion — no outage. That decides the RCA wording.

### Bound the problem
- **Implied procedure:** Before searching, establish hard upper and lower limits on where the answer can live (version range, time window, magnitude); search only inside the bounds; re-derive bounds, not conclusions, when the search fails.
- **Replaces:** Don't search everywhere — first prove the answer must lie within these limits, then exhaust that space, and widen the limits (not the guess) if it's not there.
- **Ambiguity:** "Bound" also means to bound toward (motion) and to bound a system (interfaces); context carries it, but say "establish bounds" to be safe.
- **Directive:** Bound it first: the divergence entered between tags v2.1 and v2.2 and after 09:00 — nothing outside that box gets investigated.

### Dependency-ordered sequencing
- **Implied procedure:** Order the steps as a topological sort over their dependency graph: no step executes before any of its prerequisites; detect and break cycles explicitly rather than by reordering silently.
- **Replaces:** Put the steps in an order where nothing runs before something it depends on — and when two steps circularly depend on each other, surface that conflict, don't shuffle around it.
- **Ambiguity:** Seed-verb "sequence" alone lacks the criterion; "prioritize" (value-ordered) is a different ordering key — say which key orders the list.
- **Directive:** Sequence the rollout topologically on the service graph; any cycle gets escalated with the two edges that cause it, not resolved by fiat.

### Exhaustive enumeration
- **Implied procedure:** Define the set's closure rule; enumerate every member; verify the count against an independently derived total; report the inability to close as a finding in itself.
- **Replaces:** List all of them — and "all" means: state the rule that generates the set, list until the rule is exhausted, then check the count a second way to prove nothing's missing.
- **Ambiguity:** "Exhaustive" without a closure rule is a mood, not a method; the verification-of-completeness step is the part everyone skips and the part that matters.
- **Directive:** Exhaustively enumerate the consumers of this topic: derive the list from the registry, then reconcile the count against the connection stats — the delta is the finding.

### Pareto discipline
- **Implied procedure:** Evaluate changes for Pareto dominance: adopt only moves that improve some objective without worsening any protected objective; explicit which objectives are protected and what trade-offs are licensed.
- **Replaces:** Improve the thing you're targeting without silently making anything else worse — and state up front which dimensions are protected from trade.
- **Ambiguity:** Three-way fork: Pareto optimality (decision theory) vs. the 80/20 principle (concentration of effect) vs. the distribution — speakers routinely mean 80/20 while listeners hear decision theory. Name the sense.
- **Directive:** Pareto-check the caching change: latency may improve, but memory ceiling and staleness budget are protected objectives — any regression there kills it.

### Sanity check
- **Implied procedure:** Apply a cheap plausibility gate — units, signs, magnitudes, limiting cases — before committing the expensive work; explicitly labeled as a gate, not a verification.
- **Replaces:** Before anyone invests in this, confirm it passes the obvious tests: units multiply out, the sign is right, the extreme cases behave, the magnitude isn't absurd.
- **Ambiguity:** Over-trusted because it rhymes with verification; it can only reject the absurd, never certify the correct — label it a gate or it silently becomes the whole QA plan.
- **Directive:** Sanity-check the migration estimate against row count × per-row latency; if it says 40 minutes where the window is 5, stop before planning anything.

## 3. Intelligence & Adversarial Tradecraft
*Source fields: intelligence analysis, red-teaming, security research.*

### Adversarial review
- **Implied procedure:** Adopt the hostile reader's stance deliberately: seek counterexamples, edge cases, and unstated assumptions; every paragraph must survive an intelligent attacker; approval is the output only of surviving attack.
- **Replaces:** Review this as an enemy, not an editor: your job is to break it — find the input that crashes it, the assumption that's false, the claim that dissolves under one counterexample.
- **Ambiguity:** Decays into ordinary review when the reviewer starts summarizing instead of attacking; assign the attack explicitly and forbid summary in the output.
- **Directive:** Adversarial review of the auth flow: assume I'm the attacker with the docs, a valid account, and patience — enumerate what I'd try first, second, third.

### Steelman
- **Implied procedure:** Before responding to a position, reconstruct its strongest form — stronger than its own advocates state it — including its best evidence; respond only to that reconstruction, and flag where you strengthened it.
- **Replaces:** Build the best possible version of the opposing argument before you argue against it; if your rebuttal only works on the dumb version, you haven't earned a conclusion.
- **Ambiguity:** Frequently confused with strawman (its opposite); also read as "agree with" — steelmanning is hostile in the honorable sense: you defeat the best version or you concede.
- **Directive:** Steelman the "no migration" position until its author would say "yes, exactly that" — then answer that version in the proposal.

### Red team
- **Implied procedure:** Constitute an independent group with the adversary's capabilities and freedom; charter them to defeat the plan or system, not to review it; their findings feed the defense with reproduction steps; they never grade their own fixes.
- **Replaces:** Assign people whose only job is to break this, with real adversary techniques and no stake in its success, and make the plan iterate until the attackers stop finding killers.
- **Ambiguity:** Offensive-simulation sense vs. internal critical-review sense vs. cyber range exercise; "tiger team" narrows to an elite unit on one assigned objective; state the charter and rules of engagement.
- **Directive:** Red-team the rollout plan for one day: your deliverable is the three ways production dies, each with a repro and a detection gap.

### Devil's advocate
- **Implied procedure:** Assign one participant the explicit role of opposing the emerging consensus; they argue the strongest counter-case regardless of personal belief; the role rotates; timeboxed so dissent is procedural, not personal.
- **Replaces:** Someone must argue against this decision even if everyone agrees — assigned, official, and rotated, so the group hears the counter-case before it commits.
- **Ambiguity:** Token-dissent failure mode: the assigned advocate phones it in and the ritual launders the decision; weaker than red-teaming (no execution capability, only argument).
- **Directive:** You're the devil's advocate on the monolith split: argue the strongest case for staying, in writing, before we vote.

### Premortem
- **Implied procedure:** Assume the effort has already failed; generate the specific story of its death; rank causes by likelihood × damage; convert the top causes into abort criteria and mitigations before starting.
- **Replaces:** It's a year later and this project failed spectacularly — write the postmortem now. List what killed it, pick the most probable killers, and install the tripwires that would have caught them.
- **Ambiguity:** Requires the completed-failure stance, not a polite risk list ("some risks exist" is the failure mode of the premortem itself); distinct from postmortem (after the fact) and from generic risk review (no narrative stance).
- **Directive:** Run the premortem today: the migration lost data — write that postmortem, then tell me which of its causes we tripwire and which we just accept.

### Analysis of competing hypotheses (ACH)
- **Implied procedure:** Generate multiple hypotheses simultaneously; build the evidence-by-hypothesis matrix; score every item of evidence for consistency and diagnosticity against every hypothesis; retain the hypothesis least inconsistent with evidence — not the first one that fits; record what would falsify the survivor.
- **Replaces:** List several rival explanations up front, then check every piece of evidence against each of them, and keep the one the evidence contradicts least — kill a hypothesis only with contrary evidence, never with neglect.
- **Ambiguity:** The name is invoked far more often than the matrix is executed; collapses into "brainstorm alternatives" without the scoring discipline; Heuer's tradecraft standard from intelligence analysis.
- **Directive:** Run a full ACH on the latency regression: minimum four hypotheses, the consistency matrix, and name the single most diagnostic measurement we're missing.

### Key assumptions check
- **Implied procedure:** Surface the assumptions the plan cannot survive without; rank them by load-bearing-ness × uncertainty; verify or stress-test the top ones before commitment; publish the survivors as standing tripwires.
- **Replaces:** List everything this plan silently assumes, mark which of those would sink us if wrong, and go verify the dangerous ones now rather than discover them in production.
- **Ambiguity:** Reads as boilerplate when the output isn't ranked; the deliverable is a short ranked list with verification status, not a comprehensive-feeling dump.
- **Directive:** Key-assumptions check on the cutover plan: top five assumptions, each marked verified / tested / naked — we don't proceed with any naked load-bearers.

### Diagnosticity
- **Implied procedure:** For each candidate measurement, ask which pairs of hypotheses it distinguishes; prefer evidence whose results differ across rival hypotheses; deprioritize evidence consistent with all of them no matter how abundant.
- **Replaces:** Judge every proposed test by whether its outcome would look different under each rival explanation — a test that comes out the same either way is not evidence, it's theater.
- **Ambiguity:** Rare outside analytic tradecraft — define inline on first use; easily conflated with mere "usefulness" of evidence.
- **Directive:** Rank the proposed probes by diagnosticity: heap-vs-driver must split the two hypotheses; CPU count doesn't discriminate and drops out.

### Threat model
- **Implied procedure:** Enumerate adversaries with capability and motive; enumerate assets and trust boundaries; map attack paths across the boundaries; rank by likelihood × impact; derive controls per path; revisit when any input changes.
- **Replaces:** Before securing this, say who attacks it, what they want, what they can reach, and by what path — then defend the ranked paths, not the perimeter decoration.
- **Ambiguity:** Framework-branded variants (STRIDE, attack trees) imply different outputs; a threat model without ranked paths and derived controls is a diagram, not a model.
- **Directive:** Threat-model the webhook endpoint: adversary classes, trust boundaries, the five likeliest abuse paths, and the control that kills each — one page.

### Attack tree
- **Implied procedure:** Root the tree at the adversary's goal; decompose into sub-goals joined by AND (all required) and OR (alternatives); annotate leaves with cost and feasibility; cut the cheapest-to-attacker branches first.
- **Replaces:** Draw the attacker's plan as a tree: which steps are alternatives, which must all succeed, how expensive each is — then break the cheapest links, not the most dramatic ones.
- **Ambiguity:** Not a defense artifact — an offense artifact used to prioritize defense; leaves without cost annotations rank nothing.
- **Directive:** Attack-tree admin takeover: OR of credential paths, each AND-decomposed; annotate leaf feasibility; our budget goes to the three cheapest attacker branches.

### Kill chain
- **Implied procedure:** Model the adversary's required sequence of stages; instrument detection or denial at each stage; prefer breaking early links (cheaper for us, costlier for them); measure resilience by links broken.
- **Replaces:** The attack has to complete several stages in order — map them, and make sure we can detect or stop it at each one, preferring the earliest points where intervention is cheap.
- **Ambiguity:** Military targeting origin; cyber kill chain (recon→weaponize→deliver→exploit→install→C2→act) is the common reference; "break any link" can license perimeter-only thinking if early-link detection is weak.
- **Directive:** Kill-chain the phish path: for each stage from lure to exfiltration, name the detector and the blocker — any stage with neither is our gap.

### Indicators and warnings (I&W)
- **Implied procedure:** Predefine observable precursors of each bad outcome; bind each to a threshold and an owner and a pre-authorized action; treat threshold crossings as the trigger to act, not to discuss.
- **Replaces:** Decide now, while calm, which early signals mean trouble is starting, what number each must hit, and who does what the moment it hits — so the response isn't designed during the fire.
- **Ambiguity:** Distinct from a tripwire (the single sensor) — I&W is the doctrine: precursor list, thresholds, bound actions; diluted when indicators lack pre-committed responses.
- **Directive:** Publish I&W for the migration window: queue depth > 5k for 3 min or error rate > 0.5% → on-call executes rollback, no meeting.

### Mirror-imaging guard
- **Implied procedure:** Flag every inference that assumes the other party (adversary, user, system) shares your rationality, values, or constraints; replace with observed-behavior-based inference; assign someone to challenge all such attributions.
- **Replaces:** Stop assuming the attacker values what you value or reasons as you reason — every claim about their motives needs to come from their observed behavior, not from projection.
- **Ambiguity:** Classic intelligence-analysis term; the guard is procedural (a review pass), not an attitude; also applies to users ("nobody would paste a 40MB file") and systems.
- **Directive:** Run the mirror-imaging pass on the threat model: strike any adversary attribute derived from what we would do, keep only what their telemetry shows.

### Wargame / tabletop exercise
- **Implied procedure:** Simulate execution with humans in role (including an adversary and chance events); walk the clock forward decision by decision; log decisions and their triggers; harvest the divergence between plan and play.
- **Replaces:** Before doing it live, act it out: assign the roles, inject the surprises, make people actually decide under the clock, and collect every place the plan broke.
- **Ambiguity:** Distinct from a drill (rehearsing known moves) — wargaming introduces an intelligent opponent and contingency; without injected surprise it decays to a read-through.
- **Directive:** Tabletop the launch at 14:00: you're the CDN, you're the payment provider, I inject two failures; every decision gets logged with its trigger.

### Chaos engineering
- **Implied procedure:** State the resilience hypothesis; define the steady-state metric and blast radius; inject the failure in the smallest dose that tests it; abort on threshold breach; institutionalize the learning.
- **Replaces:** Deliberately break things in production-like conditions to prove the system survives — but with a stated hypothesis, a measured steady state, and a kill switch, not vandalism.
- **Ambiguity:** Without hypothesis and blast radius it is just an outage with a press release; "game day" variants differ mainly in scope and audience.
- **Directive:** Chaos experiment: hypothesis "orders survive single-AZ loss"; steady state = order success rate; abort if success drops 1%; run in the canary region first.

### Fuzzing
- **Implied procedure:** Generate malformed, boundary, and random inputs programmatically; feed them continuously; treat every crash, hang, or invariant breach as a reproducing bug; minimize each reproducer before filing.
- **Replaces:** Have the machine attack the input layer: millions of broken inputs, run forever, every crash captured with a minimized repro — don't hand-write the weird cases a human would think of.
- **Ambiguity:** Coverage-guided vs. dumb fuzzing differ enormously in yield; fuzzing tests robustness, not correctness — a fuzzer-clean program can still compute the wrong answer happily.
- **Directive:** Fuzz the parser for 24h with the seed corpus from the old failures; minimize and file anything that panics, leaks, or hangs.

### Canary trap / barium meal
- **Implied procedure:** Issue distinctive but plausible variants of the sensitive content to each recipient; when a leak appears, diff it against the variants; the diff names the channel of origination.
- **Replaces:** Give each person a slightly different version of the document so that when it leaks, the wording itself tells you whose copy leaked.
- **Ambiguity:** Different from a canary token (an artifact that alerts when touched) — this identifies the leaking *channel* after the fact; ethics and trust costs are real; also "canary" polysemy applies.
- **Directive:** Barium-meal the roadmap: three recipient-specific wording variants; if it surfaces publicly, the diff is our leak channel.
## 4. Failure Discipline & Recovery
*Source fields: systems and safety engineering, safety-critical industries.*

### Fail closed
- **Implied procedure:** Enumerate the failure modes (crash, timeout, corrupt state, dependency death); define the restrictive state for each; on any failure enter it automatically; log the transition; require explicit action to recover.
- **Replaces:** When anything goes wrong, deny by default: lock the gate, stop the job, refuse the request — and stay locked until a human or a validated recovery path opens it.
- **Ambiguity:** Availability is the price — fail-closed systems are DoS-able by their own failure detectors; "fail secure" is the physical-security twin; must define whether timeouts count as failures (they must).
- **Directive:** The webhook verifier fails closed: any signature-check exception → reject and queue for review; no exception path admits an unsigned request.

### Fail open
- **Implied procedure:** Same enumeration, opposite default: on failure, take the permissive branch chosen deliberately because availability outranks the protected property in this context; alarm loudly while open.
- **Replaces:** If this component dies, let traffic through rather than block it — we accept that risk knowingly for availability's sake, but scream while it's degraded.
- **Ambiguity:** Usually a bug label ("the firewall failed open"), occasionally the right design; the deliberateness is the difference — an undocumented fail-open is an incident waiting to file itself.
- **Directive:** Rate limiter fails open on Redis loss — degraded and alarmed, with a 60s cap before we re-evaluate; anything else fails closed.

### Graceful degradation
- **Implied procedure:** Rank features by criticality; when capacity fails, shed features strictly in reverse criticality order while the core contract holds; never degrade by crashing; advertise degraded mode to callers.
- **Replaces:** When parts of the system die, turn off the least important features first and keep the essential promise working — a partially working system beats an error page.
- **Ambiguity:** "Fail-safe" describes the end state, this describes the trajectory; without pre-ranked features, degradation becomes improvisation; silent degradation hides rot — it must be observable.
- **Directive:** Degrade gracefully: recommendations down → serve popular; search down → serve stale index; cart and checkout are never sacrificed, and the degraded banner goes up.

### Circuit breaker
- **Implied procedure:** Count consecutive failures per dependency; past threshold, trip to open (calls rejected instantly); after a cooldown, admit one probe call; on success close, on failure reopen; trips are visible, not silent.
- **Replaces:** Stop hammering the dying service: after N failures, stop calling it entirely for a while, let one test call through later, and resume only if that succeeds.
- **Ambiguity:** Electrical heritage misread as "delete the dependency"; per-dependency state is the design point — one global breaker recreates the cascade it exists to stop.
- **Directive:** Circuit-break the payments call: trip at 5 consecutive 5xx, 30s cooldown, single probe on close; page if it re-trips 3× in 10 min.

### Watchdog / heartbeat
- **Implied procedure:** A liveness signal pulses on a fixed interval; an independent monitor watches for silence past a timeout and intervenes (restart, failover, escalate) without asking the watched component.
- **Replaces:** The worker must prove it's alive every 10 seconds — and a separate, simpler process that doesn't trust it takes action the moment the proof stops arriving.
- **Ambiguity:** Liveness is not health (a wedged loop can heartbeat); the monitor must be independent in process and failure modes or it dies with its charge.
- **Directive:** Heartbeat every 10s from the ingest worker; watchdog restarts it after 3 missed beats and pages if a restart loop forms.

### Kill switch / e-stop
- **Implied procedure:** Maintain one always-available action that halts the operation immediately and unconditionally; it works under degraded conditions; its authority overrides all other state; it is tested regularly.
- **Replaces:** There must be a big red button that stops everything, instantly, no questions, that works even when everything else is broken — and everyone knows where it is and that it works.
- **Ambiguity:** Distinguish from dead man's switch (fires on lost contact) and from abort criteria (pre-committed conditions); an untested kill switch is decorative.
- **Directive:** Every batch job registers a kill switch env var; the on-call may pull it mid-run without approval — test that monthly.

### Dead man's switch
- **Implied procedure:** The safe action fires automatically when the expected signal stops — absence of contact is treated as mandate to act; timeout and default action are fixed in advance.
- **Replaces:** If the controller goes silent, assume the worst and take the safe action automatically — safety must not depend on someone noticing the silence.
- **Ambiguity:** Inverse of the watchdog (which acts on observed death, this acts on unobserved life); punitive/whistleblowing sense exists; "fail-closed on timeout" is the engineering content.
- **Directive:** The cert-rotation job is a dead man's switch: no weekly success signal by Friday 12:00 → auto-open the incident.

### Interlock
- **Implied procedure:** Enforce a logical precondition that makes unsafe combinations impossible to request: the action physically or logically cannot begin while the precondition is unmet; no warning path exists.
- **Replaces:** Wire the constraints into the mechanics so the dangerous combination can't even be attempted — the deploy cannot start while the tests are red, by construction.
- **Ambiguity:** Often implemented as policy warnings (which are not interlocks); "permissive" is the control-systems cousin (conditions that must ALL hold to grant).
- **Directive:** Interlock deploys on green CI: the deploy API returns 409 while any required check is red — no override flag exists.

### Abort criteria / trigger points
- **Implied procedure:** Before execution, commit to measurable conditions that halt it; write them where the executor can see them mid-flight; on trigger, stop immediately and preserve state — no mid-run renegotiation.
- **Replaces:** Decide now what readings mean stop — and when you hit one, halt and keep the scene intact for diagnosis; don't negotiate with yourself while the fire grows.
- **Ambiguity:** Distinct from exit criteria (completion conditions — §8) and I&W (monitoring doctrine); criteria stated without numbers ("if it looks bad") are decoration.
- **Directive:** Load test abort criteria: error rate > 1% or p95 > 800ms or any 5xx spike — halt, snapshot, report; we diagnose after the halt, never during.

### Backout plan
- **Implied procedure:** Design and rehearse the return path to the last known-good state before committing; measure its runtime; if backout exceeds the change window or depends on untested steps, the change does not proceed.
- **Replaces:** Know how you'll undo this before you do it — actually rehearsed, actually fast enough for the window, or the change doesn't ship.
- **Ambiguity:** Distinct from rollback (the mechanism) — this is the committed, rehearsed plan including humans and comms; a backout that's "reversible in principle" is not a plan.
- **Directive:** No cutover without a backout rehearsed in staging this week: under 10 minutes, one operator, no data loss — attach the staging timing to the change ticket.

### Rollback vs. roll forward
- **Implied procedure:** On failure, choose the recovery direction deliberately: return to last good state (rollback) when the change is reversible and data permits; push the fix through (roll forward) when the forward path is shorter and safer; decide by data compatibility, not by embarrassment.
- **Replaces:** When it breaks, decide consciously: go back to the old version or push the fix forward — the data schema determines which is actually possible, and shame is not an input.
- **Ambiguity:** Roll forward as casual euphemism for "we couldn't go back" hides a schema-design failure worth its own incident line; irreversible migrations convert this choice into a one-way door.
- **Directive:** Rollback is primary for tonight's deploy — schema is additive; if data written post-deploy blocks it, say so on the ticket before we start, not after.

### Margin of safety
- **Implied procedure:** Size capacity beyond the expected worst case by a stated factor; derive the factor from uncertainty, not hope; consume margin knowingly and account for it after each consumption.
- **Replaces:** Plan for more than you think you need by a factor you can defend — and when you eat into that buffer, log it, because unlogged margin is already gone.
- **Ambiguity:** Engineering-culture term (structural origin) without a default number — the factor must be stated or it becomes vibes; distinct from "buffer" (schedule) and contingency reserve (planned slack for known unknowns).
- **Directive:** Provision 2× headroom over p99 load; if we operate above 1.5× for a week, capacity review is automatic.

### Single-point-of-failure audit
- **Implied procedure:** Trace every critical path; mark each component whose individual failure stops the path; for each marked component, verify redundancy or an accepted-risk record; unrecorded SPOFs are findings.
- **Replaces:** Walk every path that matters and find the one thing whose death takes it down alone — then either double that thing or write down why we accept the risk.
- **Ambiguity:** Human SPOFs (the one person who knows the system) hide from architecture diagrams — audit roles and knowledge too; shared-fate "redundancy" (two copies, one DNS server) doesn't count.
- **Directive:** SPOF audit of the checkout path, including people: every box gets redundant-or-accepted-risk; "Bob knows how" is neither.

### ALARP (as low as reasonably practicable)
- **Implied procedure:** Reduce risk until further reduction requires resources grossly disproportionate to the benefit gained; document the point where you stopped and the disproportion argument; revisit on change.
- **Replaces:** Keep making it safer until the next step costs wildly more than the harm it prevents — and write down where and why you stopped, so the judgment is auditable.
- **Ambiguity:** UK safety-law standard with regulatory teeth, borrowed loosely elsewhere; "reasonably practicable" is a proportionality judgment that must be argued, not asserted; not a synonym for "good enough."
- **Directive:** We've ALARP'd the retry storm: remaining mitigation costs a quarter of eng time for <0.01% availability — documented, revisit at 2× traffic.

### Preempt
- **Implied procedure:** Detect the causal chain before it completes; act on the precursor to prevent, not mitigate; the earlier the intervention point on the chain, the cheaper per unit of harm avoided.
- **Replaces:** Don't wait for the failure — watch for its opening moves and cut the sequence off before the damage step arrives.
- **Ambiguity:** Preempt (act before) vs. prevent (make impossible) vs. mitigate (reduce after); in systems, preemption also means suspending a running task — disambiguate with "preempt the failure mode."
- **Directive:** Preempt the cert expiry: renewal fires at T-30 days; T-14 without success pages the on-call; expiry itself is an incident with a root cause above it.

### Anticipate
- **Implied procedure:** Enumerate the plausible futures branching from the current state; for each consequential one, precompute the response; hold the responses ready rather than improvising them later.
- **Replaces:** Think several moves ahead: list what could plausibly happen next, decide now what we'd do in each case, and have that answer standing by.
- **Ambiguity:** **Low-medium density flag:** without the enumeration-and-precompute procedure it's a wish; as a bare instruction it decays to "be aware." Demand the futures list as the artifact.
- **Directive:** Anticipate the launch's next 48 hours: top five futures, each with its pre-decided response — the list is the deliverable, not the adjective.

### Mitigate
- **Implied procedure:** With the risk accepted rather than eliminated: reduce its probability (controls) and its severity (containment, recovery); measure both axes before and after; residual risk is recorded and owned.
- **Replaces:** We're not preventing this one, so shrink it from both ends — make it less likely and less damaging — and write down how much of it still remains and whose desk it sits on.
- **Ambiguity:** Euphemism-damaged ("we mitigated concerns" = talked); distinct from avoid (eliminate exposure), transfer (insurance/outsourcing), and accept (do nothing, record it); unmeasured mitigation is untold.
- **Directive:** Mitigate the thundering herd: jitter the retries (probability), queue + shed (severity); report both axes' before/after numbers.

### Inoculate
- **Implied procedure:** Expose the system to controlled, weakened doses of its anticipated failure modes in advance; verify the response each time; escalate the dose only after the previous one is survived.
- **Replaces:** Practice getting sick before the real infection: inject small, bounded versions of each expected failure, confirm the defenses fire, and only then raise the difficulty.
- **Ambiguity:** The medical metaphor carries the dose-control and monitoring obligations — chaos without blast radius or steady-state checks is infection, not inoculation.
- **Directive:** Inoculate against region loss: drain one AZ in staging weekly; when failover is boring there, promote the drill to one production AZ.

### Safeguard
- **Implied procedure:** Wrap the asset in named, testable controls (preventive and detective) each with an owner; verify each control fires on demand; gaps between controls are documented.
- **Replaces:** Protect this with specific mechanisms we can name and test — not good intentions — and prove periodically that each one still triggers.
- **Ambiguity:** **Low density as a bare verb:** names the outcome, not the mechanism; procedurally useful only when the named-controls-and-tests content is attached. Prefer enumerating the controls.
- **Directive:** Safeguard the export path: encryption at rest (verified quarterly), PII scan (blocking, tested monthly), access log with anomaly alert — three controls, three tests.

## 5. Security & Containment
*Source fields: information security, physical security, need-to-know culture.*

### Defense in depth
- **Implied procedure:** Deploy multiple controls in series, each assuming every other control has already failed; verify the layers are independent (no shared failure mode); an attacker must defeat all; any single defeat is survivable.
- **Replaces:** Never trust one wall: stack independent safeguards so each one works even when the others are already bypassed — and check the walls don't share a foundation.
- **Ambiguity:** Layers with a common failure mode (same credential, same vendor, same config system) are theater stacked on theater; the Swiss-cheese framing (§13) is the incident-analysis view of the same idea.
- **Directive:** Defense in depth on the admin path: network policy, mTLS, RBAC, per-action audit, and rate limits — each justified assuming all others are already gone.

### Least privilege
- **Implied procedure:** Enumerate the capabilities the task actually requires; grant exactly those; scope them to resources and time; revoke on completion; verify sufficiency empirically (the task completes) rather than by assertion.
- **Replaces:** Give this job the minimum permissions it truly needs — no broader scope, no longer than needed, taken away when done — and prove the minimum was enough by running the job.
- **Ambiguity:** Over-granting "temporarily" is the chronic relapse; scope must include blast radius of credentials (where they're readable, not just what they allow).
- **Directive:** Least-privilege the migration job: one role, two tables, 4-hour TTL; the job's success under that role is the test, and anything it can't do gets a new capability request — not a wildcard.

### Blast radius containment
- **Implied procedure:** For every action, define the maximum damage domain it can affect; choose execution so the domain is bounded (namespace, shard, region, account); prefer architectures where failure of any part cannot propagate past its boundary.
- **Replaces:** Assume this will go wrong and draw the fence now: run it where the explosion can only reach this one shard — and if the fence can't be drawn, that's a design problem to surface, not a risk to accept silently.
- **Ambiguity:** Containment failures usually arrive via shared substrates (one DB, one queue, one IAM domain) that quietly connect all the "separate" boxes; proportional-restraint sense overlaps §9.
- **Directive:** Run the new parser in the sandbox namespace with its own queue: blast radius is one replica set, and nothing shared crosses the fence without review.

### Two-person rule / four-eyes principle
- **Implied procedure:** No critical action executes on one person's (or one key's) authority: a second independent party reviews and explicitly approves before execution; independence means different reporting lines and different information.
- **Replaces:** Anything this consequential requires a second set of eyes that actually examined it — a second human, separately accountable, before it happens.
- **Ambiguity:** Rubber-stamping destroys it silently (the second approver who never looks is one person with two chairs); latency cost on urgent paths needs an explicit break-glass exception.
- **Directive:** Key rotation and prod deletion are two-person actions: the agent proposes with full diff, a human approves, the runner executes — three roles, never collapsed.

### Segregation of duties
- **Implied procedure:** Split critical processes so authoring, approving, and executing are held by different actors; no single role can both create and validate; the splits are structural, not behavioral promises.
- **Replaces:** Structure this so no one person can both write the change and bless it into production — the separation is in the system's design, not in anyone's good behavior.
- **Ambiguity:** Accounting/audit origin; for agents: the drafting agent, the approving human, and the executing runner are three duties; collapses quietly as tools centralize.
- **Directive:** Segregate duties on payouts: agent computes, human approves, payment service executes, audit system reconciles — and no API token spans two roles.

### Need-to-know
- **Implied procedure:** Access to information is granted per task-relevance, not per rank or convenience; each disclosure decision names the task it serves; aggregations that create new sensitivity are themselves gated.
- **Replaces:** People (and agents) see only what their current task requires — and combining two harmless views into a sensitive one is itself a gated disclosure.
- **Ambiguity:** Culture-heavy concept: without enforcement mechanics it decays to courtesy; scope-creep inversion ("need to know everything for my task") is the standard attack on it.
- **Directive:** Scope the agent's read access to this incident's services only — cross-service logs are need-to-know and get requested per question, not granted wholesale.

### Compartmentalize
- **Implied procedure:** Partition information and capabilities into isolated cells; define the declared channels that may cross boundaries; compromise or error in one cell must be unable to read or corrupt another; test the walls.
- **Replaces:** Keep this in sealed boxes that talk only through defined doors — so one leak or one mistake stays in its box instead of touring the building.
- **Ambiguity:** Psychological sense (walling off thoughts) vs. security sense — same architecture, different motive; over-compartmentalization taxes coordination (the knowledge now can't combine).
- **Directive:** Compartmentalize the beta: each test fixture sees only its own tenant's key, and cross-tenant reads fail closed by construction, tested weekly.

### Quarantine
- **Implied procedure:** On suspicion, move the artifact or workload out of the live path into isolated holding; nothing in holding executes or propagates; holding has an owner, a review SLA, and a release criterion.
- **Replaces:** On any suspicion, pull it out of circulation into isolation — nothing in the isolation zone runs or spreads — and it comes out only through a decision, never by timeout amnesia.
- **Ambiguity:** Malware sense vs. exposure sense vs. DLQ parking (the queue variant — keep the poison-message sense distinct); "quarantine the message, not the queue" — the unit of isolation is a design decision.
- **Directive:** Quarantine any attachment the scanner flags: moved to holding bucket, no execution, seven-day review SLA, release requires a named approver.

### Air gap
- **Implied procedure:** Physically or logically sever every network path to the protected system; transfers cross the gap only by inspected, deliberate media moves; the gap's integrity is itself monitored.
- **Replaces:** No wires to this system at all — not "firewalled," not "restricted": nothing connects — and whatever crosses does so by hand, inspected, each crossing logged.
- **Ambiguity:** Metaphorical use ("logically air-gapped") describes a firewall policy, which is a different (weaker) thing with the same confidence-inducing name; covert channels (USB, supply chain) survive true gaps.
- **Directive:** The signing key lives on the air-gapped host: no network interfaces, transfers via signed media only, each transfer initiated by the two-person rule.

### Tripwire
- **Implied procedure:** Place a cheap detector directly on the path an intruder or fault must cross; any touch alerts immediately; false positives are tuned down but the path stays covered; the tripwire is separate from the protection.
- **Replaces:** Put a bell on every door they'd have to open — it doesn't stop them, but we learn about the intrusion at the first step, not the last.
- **Ambiguity:** The single sensor vs. I&W (§3) the doctrine; canary tokens are its content-forensics cousin; "tripwire on data" (a fake record that alerts on use) is the strongest form.
- **Directive:** Seed a tripwire record — fake SSN, real-looking — into the export table; any query touching it pages security immediately.

### Sandbox
- **Implied procedure:** Execute untrusted work in an environment whose resource access, network, and filesystem are restricted by construction; the escape path is assumed attempted; artifacts cross out only through explicit inspection.
- **Replaces:** Run it where it can't touch anything that matters — no network it didn't get, no files outside its box — and whatever it produces gets inspected before leaving the box.
- **Ambiguity:** Three-way fork: dev playground (convenience), security containment (adversarial), test status ("still in sandbox"); only the second implies an adversary; security sandboxes are escaped routinely — they raise cost, not certainty.
- **Directive:** The scraped plugin runs sandboxed: seccomp profile, no net except the package registry, tmpfs workspace; its output is scanned before entering the repo.

### Harden
- **Implied procedure:** Apply the cumulative checklist for this asset class — remove defaults, close unneeded surface, patch to baseline, restrict permissions, enable logging — then re-scan against the class benchmark until it passes.
- **Replaces:** Take this from factory settings to defensible: default credentials gone, unused ports closed, versions current, permissions minimal, logging on — verified against the hardening benchmark, not self-assessed.
- **Ambiguity:** Security-hardening sense vs. cryptographic hardening vs. formal-methods "memory safety" — name the benchmark (CIS, STIG, internal) or it's a mood; hardening is checklist-iterative, unlike a one-shot fix.
- **Directive:** Harden the bastion against the CIS Level 1 benchmark: every failing control becomes a ticket, and the rescan is the merge gate.

### Break-glass
- **Implied procedure:** Maintain an emergency access path that bypasses normal controls under pre-defined crisis criteria; every use is heavily logged, alarmed, and reviewed after; unused break-glass is tested periodically.
- **Replaces:** Keep a panic door that skips the approvals — but it screams when opened, someone reviews every opening afterward, and the criteria for using it were written while calm.
- **Ambiguity:** The metaphor implies rarity; routine break-glass use means the normal path is broken (a finding, not a convenience); expired credentials on break-glass accounts are a classic latent failure.
- **Directive:** Break-glass creds exist for Sev-1 only: use triggers an automatic page to security and a next-day review; quarterly drill verifies they still work.

## 6. Verification & Quality Assurance
*Source fields: science, engineering, software testing.*

### Verify vs. validate
- **Implied procedure:** Verify = check the artifact against its specification (built right); validate = check it against the actual need (built the right thing); run both, in that order; name which one each check performs.
- **Replaces:** Check it matches the spec, then separately check the spec was the right spec — these are different checks with different failure modes, and passing one says nothing about the other.
- **Ambiguity:** Heavily conflated in general use; a third sense ("validate input") means well-formedness checking — in agent directives, say "verify against spec" or "validate the shape" explicitly.
- **Directive:** Verify the parser against the spec's 214 cases, then validate the spec itself against five real customer files before we call it done.

### Reproduce
- **Implied procedure:** Starting only from the stated artifacts and steps, obtain the same result independently; any step requiring unstated context is a finding; unreproducible results are not yet results.
- **Replaces:** Make it happen again from the instructions alone — if you needed to ask the original author anything, the instructions are broken and that's part of the bug.
- **Ambiguity:** Reproduce (same result from same steps) vs. replicate (independent re-derivation, ideally different conditions); in bug work, "cannot reproduce" often means "cannot reproduce yet" — scope the attempt before declaring it.
- **Directive:** Reproduce the crash from the report alone, on a clean VM, before any theorizing; log every deviation the report failed to mention.

### Replicate
- **Implied procedure:** Re-derive the finding through an independent execution — different agent, different seeds or samples where possible; agreement across replications grades the claim's robustness; disagreement reopens it.
- **Replaces:** Have someone else get there by their own path — not rerun your script, but rebuild the measurement — and trust the claim at the level the paths agree.
- **Ambiguity:** Science's replication-vs-reproduction line is exactly reversed in some fields; in agent work: reproduce = rerun to same result, replicate = independently re-derive.
- **Directive:** Replicate the benchmark with a fresh harness and different fixtures; if your number moves more than 5%, the first number was harness luck.

### Benchmark
- **Implied procedure:** Fix the workload, dataset, metric, and environment; measure the candidate and the baseline under identical conditions; report deltas with variance, not point values; freeze the benchmark so results compare across time.
- **Replaces:** Compare like with like under a frozen, published test setup — same data, same machine class, same metric — and give me the spread, because one run of anything is noise wearing a number tag.
- **Ambiguity:** Micro vs. macro benchmarks answer different questions and are not interchangeable; Goodhart pressure (§12) bends any benchmark once it becomes a target; unversioned benchmarks rot silently.
- **Directive:** Benchmark against the frozen v3 corpus: three runs, medians and p90s, baseline pinned to the same commit — and flag any run where variance exceeds the claimed improvement.

### Cross-reference
- **Implied procedure:** Take the claim to each independent record that should reflect it; check mutual consistency field by field; divergences become findings with both sources cited; unresolved divergence is reported, never averaged.
- **Replaces:** Check this against every other place that should agree with it — and where they disagree, show both numbers and investigate; don't pick a favorite quietly.
- **Ambiguity:** Weaker than reconcile (§2): cross-reference finds the disagreement, reconcile resolves it; "see also" citation sense is a different word entirely.
- **Directive:** Cross-reference the OpenAPI spec against the actual handler routes; every divergence gets a row: source, target, discrepancy, proposed authority.

### Attest
- **Implied procedure:** Bind an identity to a signed claim about an artifact's properties at a point in time; the claim is verifiable by third parties later; attesting implies accountability for the claim's truth.
- **Replaces:** Put your name, cryptographically, on the statement that this artifact has these properties, at this time — so anyone can verify you said it and hold you to it.
- **Ambiguity:** Security-attestation sense (signed evidence, e.g., SLSA provenance) vs. ceremonial sense ("I attest that...") which carries no verifiability; specify which mechanics.
- **Directive:** Attest each release artifact: signed provenance statement (builder, inputs, commit) attached before promotion; unattested artifacts cannot pass the gate.

### Smoke test
- **Implied procedure:** Run the minimal pass/fail probe of each critical path's liveness after any change; a failure blocks everything else; passing says alive, nothing more.
- **Replaces:** Just check the thing boots and its main paths respond — this catches the catastrophic, and it is explicitly not a quality verdict, only a liveness one.
- **Ambiguity:** Over-trusted because it rhymes with testing; it's a positive control for the deployment process itself; "smoke passed" must never be read as "works."
- **Directive:** Smoke after every deploy: three canonical requests through each critical path; any failure auto-triggers the rollback, no human deliberation.

### Soak test
- **Implied procedure:** Run representative load for an extended, pre-declared duration to surface slow failure modes (leaks, fragmentation, clock drift, unbounded growth); define the resource trajectories watched and their abort lines.
- **Replaces:** Leave it running hard for hours or days and watch the curves that only misbehave over time — memory, handles, queue depth — with numbers that stop the test if they cross.
- **Ambiguity:** Distinguished from load testing (peak behavior now) and stress testing (beyond capacity to find the breaking point); without watched trajectories it's just an uptime screenshot.
- **Directive:** Soak the ingestion service 48h at 60% load: RSS, fd count, and queue depth trended; abort criteria on any monotone growth.

### Regression test
- **Implied procedure:** Maintain the executable guard for every fixed defect: the failing input that motivated each past fix stays in the suite forever; any change that re-breaks it is caught before merge; suite growth is the tax on forgetting.
- **Replaces:** Every bug we ever fixed gets a permanent test that fails if it comes back — the suite is our institutional memory of being wrong.
- **Ambiguity:** "Regression" (something that worked broke) vs. the ML sense (performance drift); the suite guards known past failures only — it is silent about novel ones.
- **Directive:** Before closing the ticket, add the reproducer as a named regression test; a fix without its test is a promise, not a repair.

### Property-based testing
- **Implied procedure:** State the invariants that must hold for all inputs (round-trip, monotonicity, bounds); generate inputs adversarially at scale; shrink every counterexample to its minimal form; the invariant list is the design artifact.
- **Replaces:** Stop writing one input at a time — write the laws the code must obey, let the machine throw millions of nasty cases at them, and get back the smallest case that breaks each law.
- **Ambiguity:** Invariants that merely restate the implementation test nothing; shrinking (minimization) is the feature that makes failures actionable; metamorphic testing (checking output relations under input transforms) is its cousin where full oracles don't exist.
- **Directive:** Property-test the codec: lossless round-trip and canonical-form invariants over generated unicode; every counterexample shrunk and filed.

### Mutation testing
- **Implied procedure:** Inject small program mutations (flip operators, delete statements); run the suite after each; a mutant that survives indicates a test gap; the surviving-mutant list is the coverage to-do.
- **Replaces:** Test the tests: break the code a little at a time and check the suite notices — every break the suite shrugs at is a hole in the suite, proven, not guessed.
- **Ambiguity:** Measures test sensitivity, not correctness (a suite can kill mutants and still bless wrong behavior); expensive at full coverage — sample the hot modules.
- **Directive:** Mutation-score the payment module: any surviving mutant in the rounding or refund logic becomes a mandatory new test before release.

### Characterization test / golden master
- **Implied procedure:** Before touching legacy behavior, capture its current outputs on a broad input set as the reference; changes must preserve the golden outputs exactly (quirks included) unless each deviation is itemized and owned.
- **Replaces:** Pin down what it does today — bugs, weirdness, and all — into an executable reference, then refactor against it; any intended behavior change is listed separately, one by one.
- **Ambiguity:** Freezes the current state including its defects — the point is separating "refactor" from "change," not certifying correctness; golden masters rot as legitimate requirements evolve.
- **Directive:** Characterize the parser before the rewrite: 10k fixture pairs recorded; the rewrite must match all of them, and its intended deviations are a reviewed list, not an accident report.

### Negative control
- **Implied procedure:** Include a case where the bug/condition is deliberately present (or absent) that must produce the known bad (or good) result; if the control doesn't behave as planted, the test can't detect anything and is void.
- **Replaces:** Prove the test can fail: reintroduce the bug on purpose and watch the suite go red — a suite that stays green with the bug planted can never tell you anything.
- **Ambiguity:** Positive control (must pass) and negative control (must fail) get swapped across fields; in agent-verification use: the control validates the detector, not the code.
- **Directive:** Add a negative control to the flake CI: revert the fix on a shadow branch nightly; the alarm must fire, or the alarm is the bug.

### Checklist discipline
- **Implied procedure:** Execute the written checklist verbatim, confirming each item by observation (not memory) before proceeding; the checklist is read-do or do-confirm by design; deviations are announced, never silent.
- **Replaces:** Follow the written list every single time, actually looking at each thing before checking it — the list catches the dumb lethal stuff that expertise skips, and skipping items quietly is how experts die.
- **Ambiguity:** Checklists discipline memory, not judgment — they encode the steps everyone "knows" and still skips; "measure twice, cut once" is the folk form; a checklist that's never been executed against a real failure is untested.
- **Directive:** Run the deploy checklist verbatim with a witness: read each item aloud, verify by observation, initial it — no item is checked from memory.

### Pre-flight check
- **Implied procedure:** Immediately before the irreversible or high-cost commitment, verify every readiness condition with fresh observations — not cached beliefs; any red stops the commit without negotiation.
- **Replaces:** One final gate right before you can't take it back: check everything is actually ready right now, with fresh eyes, and any doubt means stop.
- **Ambiguity:** Aviation heritage carries the no-negotiation property; "pre-flight" done from stale dashboards is theater — freshness of observation is the load-bearing part.
- **Directive:** Pre-flight the migration at T-0: replication lag, disk headroom, backup verified restorable, on-call acked — fresh readings, four greens, else we stand down.

### Read-back / closed-loop confirmation
- **Implied procedure:** The receiver repeats the message verbatim; the sender confirms or corrects; only confirmation completes the transmission; numbers and identifiers are digit-wise.
- **Replaces:** Repeat it back exactly before acting on it — the sender confirms you heard right — because acting on the misheard version of a command is worse than the delay.
- **Ambiguity:** Aviation/ATC and clinical handoff heritage; acknowledgment ("got it") is not read-back — agreement is not confirmed receipt; applies with full force to agent-executed commands.
- **Directive:** Closed-loop all destructive commands: echo the exact SQL and row count back; execute only on explicit confirm — "yes, that one."

### Blind analysis
- **Implied procedure:** Hide from the analyst which samples/conditions are which (expected outcome, group identity) until conclusions are recorded; label blindness is verified by a guess-rate test; unblinding happens after commitment.
- **Replaces:** The evaluator must not know which output is the new model's — labels stripped, order shuffled — and opinions get written down before anyone learns which was which.
- **Ambiguity:** Science origin; "fresh eyes" review is its weak cousin (context-naive reviewer) without the formal hiding; leakage through style/timing is the usual failure.
- **Directive:** Blind the eval: anonymize old-vs-new outputs, randomize order, record the scorer's judgments — then unblind and reconcile disagreements.
## 7. Execution & State Discipline
*Source fields: systems engineering, databases, DevOps.*

### Orchestrate
- **Implied procedure:** Decompose the outcome into independently runnable components; wire their sequencing, data flow, and failure propagation; supervise the whole flow rather than executing each part; the orchestrator owns the topology, not the payloads.
- **Replaces:** Stand up the pipeline: identify each service and script, define their inputs and outputs, connect them in dependency order, decide what happens to the whole chain when each stage fails, and supervise end to end.
- **Ambiguity:** Implies control over components you may not own (contract question); adjacent to "automate" (replacing manual steps) — orchestration is about coordination topology.
- **Directive:** Orchestrate the release: build → migrate → deploy → smoke; any stage failure halts the chain and reports which stage, which input, what state.

### Operationalize
- **Implied procedure:** Reduce the abstract goal to a metric, a threshold, a check interval, and a bound action; nothing counts as operational until a sensor and an executor exist for it; the reduction is written down as the deliverable.
- **Replaces:** Turn "we care about this" into: what number, what threshold, checked how often, and who does what when it crosses — until those four exist, we have a sentiment, not an operation.
- **Ambiguity:** Management-speak sense ("operationalize our values") omits the sensor-action decomposition and is exactly the failure mode; the four-part test is the repair.
- **Directive:** Operationalize "pipeline healthy": green = 0 failed jobs in 24h; amber = 1–3 with rerun + flag; red = page. That table is the deliverable.

### Consolidate
- **Implied procedure:** Identify the redundant variants of an artifact; select or construct the single authoritative one; migrate all consumers to it; verify by absence — no orphan copies remain writable.
- **Replaces:** Merge the copies into one source of truth: pick or write the canonical version, move every consumer onto it, and then make sure no straggler copy can still be edited into divergence.
- **Ambiguity:** Distinguish from merge (VCS mechanics) and deduplicate (data-level); consolidation without the consumer-migration-and-verification tail regrows the problem.
- **Directive:** Consolidate the four config files into one schema: migrate readers one by one, then flip the old paths read-only and alert on any write.

### Streamline
- **Implied procedure:** Map the current steps; delete or combine steps whose removal preserves the outcome; measure outcome preservation before and after; each removal is justified against the preserved invariants.
- **Replaces:** Take out every step that isn't carrying weight — and prove the result still does everything it did, by measurement, not by assumption.
- **Ambiguity:** **Medium-low density flag:** corporate use means "improve vaguely"; the procedural content is entirely in outcome-preservation measurement, which casual use omits. Demand the before/after invariant check.
- **Directive:** Streamline onboarding from 9 steps to 5: each deleted step gets a line stating which invariant now covers it; the two-week error rate is the verdict.

### Automate
- **Implied procedure:** Encode the stabilized procedure as code (it has run manually at least twice unchanged); include the failure path and the rollback; the automation is monitored like a production service; humans handle exceptions, not the happy path.
- **Replaces:** Do it by hand until it's boring, then write the code that does it — including what the code does when it fails — and watch the automation itself, because unwatched automation fails silently.
- **Ambiguity:** Automating an unstable or wrong process fossilizes the defect (the classic trap: automation is acceleration, not correction); also used as a goal-word without an object ("we should automate more").
- **Directive:** Automate the cert rotation only after three clean manual runs; the script's failure path opens a ticket, never retries unbounded.

### Idempotent
- **Implied procedure:** Define the operation's convergence state; implement so repeated application converges to that state rather than accumulating; key operations by identity; test by executing twice and diffing.
- **Replaces:** Running it again must be safe: same input, same end state, no duplicates — so a retry after a crash is free instead of a data-corruption event.
- **Ambiguity:** HTTP-verb sense ("PUT is idempotent") vs. migration idempotence vs. idempotency-key pattern; idempotent ≠ atomic (§ below) — an idempotent op can still tear mid-flight.
- **Directive:** Make the migration idempotent: re-running inserts nothing new, updates converge, and the test is literally "run twice, diff zero."

### Atomic / commit point
- **Implied procedure:** Group the state changes so no intermediate state is observable: all apply or none; define the single commit point where the change becomes real; everything before it is revertible for free, everything after is not.
- **Replaces:** Make it all-or-nothing: no reader can ever see the half-done state — and know exactly which instruction is the point of no return.
- **Ambiguity:** Physics sense (indivisible) borrowed; in distributed systems, atomic commit is a protocol (2PC) with its own liveness costs; "atomic" in casual planning use means "as one unit" — say which.
- **Directive:** The rename + repoint must be atomic: both or neither, readers see old or new; the config swap is the commit point — everything before it rolls back clean.

### Compensating action (saga)
- **Implied procedure:** Where atomic commit is impossible (cross-system, no shared transaction), define for each step an explicit semantic undo; execute steps in order; on failure run compensations in reverse; the end state is consistent, though not identical to never-started.
- **Replaces:** Since these two systems can't share a transaction, write the undo for every step before you take it — and when step 4 fails, run the undos backward from there.
- **Ambiguity:** Compensation restores consistency, not history (an email sent stays sent); silently weaker than rollback — the residual trace must be documented per step.
- **Directive:** No 2PC across the CRM and billing APIs: write compensating actions for each call in the saga, execute in order, compensate in reverse on failure, and log the residual state.

### Optimistic concurrency (compare-and-swap)
- **Implied procedure:** Read state with its version; compute the change; apply only if the version is unchanged since the read; on conflict, discard and retry from fresh state — never merge blind.
- **Replaces:** Check the world still looks like it did when you decided: apply the write only if nothing moved underneath you, and if it did, start over from the new reality.
- **Ambiguity:** Contrast with pessimistic locking (lock first, wait); retry loops under contention need backoff (§ below); the pattern's name in instruction form is "revalidate at use."
- **Directive:** CAS the config update: apply only if resourceVersion still matches what you read; on mismatch, re-read, rediff, and try once more before reporting conflict.

### Snapshot-before-mutate
- **Implied procedure:** Immediately before destructive change, capture restorable state (dump, tag, image); verify the snapshot restorable-ness; only then mutate; the snapshot outlives the change's verification window.
- **Replaces:** Take the backup you'd curse yourself for skipping — and prove it can be restored — before you touch anything you can't rebuild.
- **Ambiguity:** A snapshot without a restore test is a comfort blanket; also distinct from WAL (which records intent, not just state).
- **Directive:** Snapshot the accounts table (pg_dump, tag the file, restore-probe into a scratch DB) before the column type change — the probe is part of the snapshot.

### Write-ahead log
- **Implied procedure:** Record intended actions durably before executing them; execution follows the log; on crash, replay the log from the checkpoint; the log is the truth of intent.
- **Replaces:** Write down what you're about to do where it survives crashes, then do it — so any interruption resumes from the record instead of from guesswork.
- **Ambiguity:** Database heritage; applied to agents it means an externalized durable intent record (§18 state externalization is the general form); replay must be idempotent or the guarantee collapses.
- **Directive:** WAL the migration: append each intended DDL statement to the journal before executing; the recovery procedure replays the journal idempotently and reports position.

### Dry run
- **Implied procedure:** Execute the full path with effects suppressed or diverted to a disposable sink; capture everything the real run would do; diff intended-vs-actual; a clean dry run is the ticket's evidence, not its substitute.
- **Replaces:** Walk the whole thing through without touching anything real — show me exactly what it would do, then we compare that against what we meant.
- **Ambiguity:** Coverage varies: some dry runs skip validation, some suppress only writes; "measure twice, cut once" is the folk ancestor; a dry run in a stale environment certifies nothing.
- **Directive:** Dry-run the bulk edit: full parse and full diff against a copy; the diff is the review artifact — zero surprises at execution time is the bar.

### Side-effect isolation
- **Implied procedure:** Enumerate every mutation the work could perform; confine them to declared boundaries (paths, tables, endpoints); verify the boundary holds (read-only mounts, blocked egress); undeclared side effects are defects.
- **Replaces:** Decide up front the only places this work is allowed to change anything — and enforce that fence mechanically, so exploration can't damage what it wasn't sent to touch.
- **Ambiguity:** Boundary enforcement must be mechanical (mounts, policies), not behavioral (good intentions); research tasks need it most exactly when they feel least dangerous.
- **Directive:** Analysis is read-only: mount the repo RO, writes go to /tmp/out only, network limited to the registry; any other observed write is a bug report.

### Immutable artifact
- **Implied procedure:** Build once, name the artifact by its content hash; never modify in place; "change" means build a new artifact and repoint; rollback is repointing to a prior name.
- **Replaces:** Whatever we deploy is a frozen, content-addressed thing — you don't edit it, you build its successor and switch the pointer; reverting is just pointing back.
- **Ambiguity:** Immutable artifacts vs. immutable infrastructure (whole environments from templates); requires content addressing or signatures to mean anything under adversarial conditions.
- **Directive:** Ship the container as an immutable artifact tagged by digest; the deploy references the digest, and "hotfix in prod" is disabled by policy and by registry.

### Version pinning / lockfile
- **Implied procedure:** Fix every dependency to an exact version (digest where possible); record them in a lockfile that is itself versioned; upgrades happen as reviewed, isolated changes with their own tests; floating ranges are prohibited in CI.
- **Replaces:** Nail every dependency down exactly, keep the nails in the repo, and make upgrading a deliberate reviewed act — not something the build does to us overnight.
- **Ambiguity:** Lockfile honesty (transitives included?) varies by ecosystem; pinning without an upgrade cadence trades rot for stagnation — schedule it.
- **Directive:** Pin the toolchain in the lockfile including transitive digests; `latest` anywhere in CI is a failed check; upgrades ride their own PR with the diff suite.

### Hermetic build
- **Implied procedure:** Make outputs depend only on declared inputs: fixed toolchain, vendored deps, no network at build time, no ambient state (clock, locale, env); identical inputs produce bit-identical outputs.
- **Replaces:** The build can only use what it declares and carries — nothing from the network, nothing from the build machine's mood — so the same commit always produces the same artifact, anywhere, forever.
- **Ambiguity:** Hermetic (sealed inputs) vs. reproducible (same output) — related, not identical; timestamp/locale/locale-embedded paths are the classic leaks.
- **Directive:** Make the release build hermetic: vendored deps, fixed toolchain digests, SOURCE_DATE_EPOCH set, network disabled in the builder — then bit-compare two builds on different hosts.

### Deterministic replay
- **Implied procedure:** Record the full input stream; on demand, re-execute from a checkpoint against the recorded stream; the execution follows the identical path; divergence is itself a monitored signal.
- **Replaces:** Keep everything needed to make it happen again exactly as it happened — same inputs, same order, same result — so failures can be studied at full fidelity offline.
- **Ambiguity:** Requires disciplined capture (including time, randomness seeds, external responses); replay fidelity is only as good as the capture's completeness — unrecorded side channels break it silently.
- **Directive:** Enable deterministic replay on the order service: record ingress and external responses; any Sev-1 gets replayed in staging with assertions on the divergence points.

### Backfill
- **Implied procedure:** Apply the change retroactively to historical records: define the transformation, the batch boundaries, and the idempotency key; run incrementally with checkpoints; verify counts and samples old-vs-new; the backfill is re-runnable after interruption.
- **Replaces:** Fix the old data too, not just the code: run the transformation over history in resumable batches, prove the row counts and spot-checks agree, and make sure an interrupted run can just be started again.
- **Ambiguity:** Forward-fix vs. backfill semantics must be stated (does the new code handle old rows, or does the migration rewrite them?); silent dual-code-paths during the window are the trap.
- **Directive:** Backfill the currency field in 10k-row batches keyed by id: checkpointed, idempotent, count-reconciled — and the old reader path stays until the backfill reports 100% twice.

### Rectify
- **Implied procedure:** Detect the deviation from correct state; restore correctness; then verify the restoration by measurement against the correct-state definition; the word claims the error is gone, not merely addressed.
- **Replaces:** Put it back to right — and then check it's actually right against the definition of right, because "I did a fix" and "it is correct now" are different claims.
- **Ambiguity:** Weaker uses mean "adjusted"; the repair-verify pairing is the procedural core; silently conflated with remediate (fixing the class, § below).
- **Directive:** Rectify the drifted shard: re-sync from primary, then diff row counts and checksums — the verification is the completion criterion, not the sync command's exit code.

### Remediate
- **Implied procedure:** Beyond fixing the instance: identify the class of defect, remove the class (control, generator, pattern), and verify by searching for siblings of the same class; the same defect cannot recur through that path.
- **Replaces:** Don't just patch this one — find every other place this same mistake lives, fix the mechanism that produced them, and sweep to prove no siblings remain.
- **Ambiguity:** Security-remediation sense (close the vuln class) vs. HR sense (rehabilitate a person); distinct from rectify (instance) — remediation targets the class; "rehabilitate" as a sibling term is best reserved for restoring a compromised account/system to trust.
- **Directive:** The off-by-one is fixed — now remediate: grep for the pattern that generated it, fix all five call sites, and add the lint rule that makes the class unrepresentable.

### Normalize
- **Implied procedure:** Map every equivalent representation to the single canonical form before comparison, storage, or deduplication; the normalization rules are explicit and versioned; transformations are idempotent.
- **Replaces:** Make everything that means the same thing look the same way first — one canonical encoding, applied identically everywhere — or your comparisons lie to you.
- **Ambiguity:** Canonicalization sense vs. statistical normalization (scaling) vs. the failure to normalize deviance (§12 — opposite valence entirely); "canonical" (§17) names the chosen form.
- **Directive:** Normalize keys to NFC snake_case before the merge; the rule table is versioned in the repo, and the dedup count is reported before we drop rows.

### Backoff with jitter
- **Implied procedure:** On retryable failure, wait an exponentially growing interval with a random component (jitter) added; cap the total attempts and the total time; non-retryable failures bypass the loop entirely.
- **Replaces:** When it fails, wait a bit longer each time plus some randomness — so a thousand synchronized clients don't hammer in lockstep — and give up after a stated number of tries.
- **Ambiguity:** The jitter is the part everyone drops, and it's the part that prevents thundering herds; exponential-without-jitter is synchronized self-harm; retry budgets vs. attempt caps differ.
- **Directive:** Retry the upstream with backoff and jitter: base 200ms, ×2, ±30% jitter, 5 attempts max, then circuit-break and report.

### TOCTOU guard (revalidate at use)
- **Implied procedure:** Whatever was validated at check time is revalidated at use time: the world is allowed to change between your check and your action, so bind the check's result to the action's input.
- **Replaces:** Look again right before you leap — between when you checked the condition and when you act on it, the condition may have died; check-and-act must be one atomic motion.
- **Ambiguity:** Security-heritage acronym (time-of-check to time-of-use) opaque to newcomers — the parenthetical expansion is the usable form; race-condition framing makes the fix (locking or CAS) clearer.
- **Directive:** TOCTOU guard the cleanup: re-stat and re-verify the path is still the scanned file inside the unlink, or hold the fd you validated.

## 8. Planning & Strategy
*Source fields: military doctrine, project management, product practice.*

### Delineate
- **Implied procedure:** Draw the explicit boundary of the work: what is in, what is out, and the interface between them; the out-list is written, not implied; boundary disputes are resolved by consulting the delineation, not by renegotiating silently.
- **Replaces:** Write down exactly where this task's responsibility starts and stops — with an explicit not-this list — so expansions have a document to violate instead of a vibe to argue with.
- **Ambiguity:** Medium density: the artifact (the written boundary) is the value; without the out-list it's a synonym for "describe."
- **Directive:** Delineate the integration task: in-scope = auth and sync; out-of-scope = billing UI, reporting, schema redesign; anything else found gets a decision, not a shrug and absorption.

### Prioritize
- **Implied procedure:** Rank the items by a declared key (value × urgency × dependency-blocking); break ties by the key, not by requester volume; the ranking is visible and re-derived when inputs change.
- **Replaces:** Put these in a defensible order and tell me the rule you used — because "everything's important" is a scheduling deadlock, and loudest-voice is the default key we're replacing.
- **Ambiguity:** Without the declared key it's a power move, not a procedure; priority-inversion (low-key items blocking high-key ones through dependencies) is the classic failure of naive ranking.
- **Directive:** Prioritize the backlog by blocked-downstream × revenue-at-risk; publish the sort key with the list, and flag any item whose rank is a judgment call.

### Working backwards
- **Implied procedure:** Write the finished outcome first (the press release, the user story in the past tense); derive from it the minimum set of deliverables; each deliverable justifies itself by trace to the outcome or gets cut.
- **Replaces:** Describe the end state as if it already exists, then work out what must be true for that sentence to be honest — everything that doesn't make the sentence true is out of scope.
- **Ambiguity:** Distinct from inversion (§2: reason from failure) — this is derivation from the finished state; product-heritage (press-release method); without the trace-to-outcome step it decays to vision-statement theater.
- **Directive:** Write the launch press release first; every workstream must cite the sentence it makes true, or it's cut.

### End state / exit criteria
- **Implied procedure:** Define completion as observable conditions checked against reality (not activities performed); the criteria are fixed before execution starts; work ends when they hold, regardless of remaining enthusiasm.
- **Replaces:** Define "done" as measurable states of the world — then stop when the world is in that state; we don't stop when the tasks run out, and we don't continue because the tasks were fun.
- **Ambiguity:** Exit criteria (we may stop) vs. acceptance criteria (the deliverable qualifies) vs. abort criteria (§4: we must stop); tasks-completed is the counterfeit version of all three.
- **Directive:** Exit criteria for the incident: error budget restored, cause identified with evidence, one preventive action merged. Not "postmortem written" — that's an activity, not a state.

### Definition of done
- **Implied procedure:** Attach to each unit of work a fixed completion checklist (tests, docs, review, telemetry, rollback path); the unit is not done until every item holds; the list is identical across units, changed only by process decision.
- **Replaces:** "Done" means the same thing every time: tested, reviewed, documented, observable, reversible — not "the code is written," which is where amateurs put the finish line.
- **Ambiguity:** DoD (per-unit quality bar) vs. exit criteria (per-effort end state) vs. acceptance criteria (per-deliverable contract); a DoD nobody verifies on merge is a poster.
- **Directive:** Definition of done here: tests green, README updated, metric emitted, rollback documented — the PR template enforces all four checkboxes, and "partial done" doesn't parse.

### Courses of action (COA) development
- **Implied procedure:** Generate genuinely distinct candidate plans (not variants of the first); state each one's assumptions, cost, and failure signature; wargame each against the criteria; select the survivor with the rejected options recorded.
- **Replaces:** Build at least three actually-different ways to do this, pressure-test each against our constraints and failure scenarios, choose one, and keep the losers on file with the reason they lost.
- **Ambiguity:** Military planning heritage; the common decay is three costumes on one plan; the recorded-rejection step is what keeps it honest when circumstances change.
- **Directive:** Three COAs for the capacity crunch (split service, cache aggressively, buy hardware): assumptions, cost, failure mode each; wargame against Black-Friday load; document the selection.

### Branches and sequels
- **Implied procedure:** Identify the foreseen decision points; preplan the alternative taken at each (branch) and the follow-on after success (sequel); the plan carries its own decision tree; at the point, you choose, you don't design.
- **Replaces:** Decide now what we'll do if the cheap path fails at each known fork, and what we'll do next if it succeeds — so the future decision is a selection among prepared moves, not an all-hands panic.
- **Ambiguity:** Military doctrinal terms; adjacent to implementation intentions (if-then precommitments) in psychology; branches without named decision points drift into generic contingency lists.
- **Directive:** Branches for the rollout: 5xx at canary → hold, shard by cohort, or abort — each fully specified. Sequel on clean 24h: full fleet by Friday.

### Critical path
- **Implied procedure:** Build the dependency graph with durations; compute the longest chain to completion; that chain's slack is zero — protect it, staff it, and re-derive it when any node moves; delays off-path are recoverable, delays on-path are not.
- **Replaces:** Find the chain of tasks where every day lost is a day lost forever — that's where attention and people go first; everything else has slack and can wait.
- **Ambiguity:** Critical-chain variant folds resource contention into the path; the method's honesty depends on duration estimates, which are chronically optimistic (§12 outside view applies).
- **Directive:** Recompute the critical path weekly; anything that lands on it gets its own risk line in the status; off-path slippage gets one sentence.

### Main effort / economy of force
- **Implied procedure:** Name the one decisive task that receives priority of scarce resources; every other task gets the minimum that keeps it viable; resource conflicts resolve toward the main effort by standing rule.
- **Replaces:** Pick the thing that decides this week and concentrate everything on it — everything else runs on fumes by design, and that's not neglect, it's arithmetic.
- **Ambiguity:** Military doctrine heritage; misread as "prioritize" (ranking) — this is allocation plus a conflict-resolution rule; without a named single main effort, everything is the main effort and nothing is.
- **Directive:** Main effort this month is checkout latency: conflicts resolve toward it; reporting and feature polish get minimum-viable hours, recorded as deliberate, not accidental.

### Timebox
- **Implied procedure:** Fix the duration and let scope flex: when the box ends, work stops and the deliverable is whatever honestly exists; the box's end is a hard stop, pre-agreed, with results reported either way.
- **Replaces:** You have exactly this long — when it's up, you stop and show what you have; scope is the variable, the clock isn't, and "almost" counts as done-with-gaps to report.
- **Ambiguity:** Not a deadline (scope fixed, date flexes) — the inversion matters; timeboxing exploration prevents rabbit holes, but timeboxing surgery would be insane — match the tool to the reversibility of the work.
- **Directive:** Timebox the parser investigation to 4 hours: at the bell, report findings, confidence, and recommended next box — not a half-finished rewrite.

### Spike (timeboxed exploration)
- **Implied procedure:** Run a bounded experiment whose deliverable is knowledge, not production code: state the question, the time budget, and the decision the answer feeds; the artifact is discarded or rebuilt to standard afterward.
- **Replaces:** Go find out cheaply whether this approach can work — fixed hours, one question to answer, and whatever code you write to learn it gets thrown away or rewritten properly.
- **Ambiguity:** The discard clause is the most-violated term (spikes graduate into production by inertia); traffic-spike polysemy applies; a spike without a decision it feeds is tourism.
- **Directive:** Two-day spike: can the JIT handle our IR? Answer by Friday with a recommendation and a number; the prototype code is already scheduled for deletion.

### Tracer bullet / walking skeleton
- **Implied procedure:** Before optimizing any single stage, drive one thin real instance end-to-end through every stage with production-shape interfaces; fix only what blocks passage; then widen each stage in place.
- **Replaces:** Get one real request all the way through the whole pipeline first — ugly but genuine, every stage touched — because integrating skeletons early is cheap and integrating Big Bangs never happens.
- **Ambiguity:** Analog, not literal ordnance; distinct from prototype (which explores feasibility) — this builds the real structure thinly; the discipline is resisting stage-local perfection.
- **Directive:** Tracer first: one genuine order from webhook to ledger through the real services and schemas; only then does any stage get tuned.

### Go/no-go gate
- **Implied procedure:** Schedule the decision point with named criteria and a named decider; evidence is presented against each criterion; a single unmet criterion is a no-go unless the decider explicitly waives it with a recorded reason.
- **Replaces:** At this checkpoint we stop and decide with a checklist: every criterion shown, someone accountable says go or no-go, and any waiver is written down with who and why.
- **Ambiguity:** Gate criteria without owners decay into group nodding; distinct from abort criteria (mid-flight stops); "go with conditions" should mean conditions with owners and dates or it means nothing.
- **Directive:** Go/no-go Friday 15:00: replication lag < 2s, backup restored in staging, on-call briefed, rollback rehearsed. Any red stops us; waivers need the EM's name on them.

### Scope containment
- **Implied procedure:** Hold work to the delineated objective: discovered adjacent work is logged, triaged, and scheduled — not absorbed; the standing question is "does this serve the stated objective," and the default answer to expansion is a new ticket.
- **Replaces:** When you find more work than you were given, write it down and hand it back — don't do it silently; the task either finishes as defined or the definition changes through an explicit decision.
- **Ambiguity:** Over-tight containment blocks legitimately discovered prerequisites — the repair is escalation and re-scoping, not silent refusal; distinguish scope creep (expansion) from gold-plating (unrequested polish).
- **Directive:** Scope stays the stated objective: anything discovered that doesn't serve it gets a ticket and one summary line — the fifth such line triggers a scope conversation with the owner.

### Two-way vs. one-way doors
- **Implied procedure:** Classify each decision by reversibility: two-way (cheap to undo) → decide fast with partial information; one-way (expensive or impossible to undo) → deliberate, verify, and get independent review; when in doubt, run the cheap experiment that converts one-way to two-way.
- **Replaces:** Is this reversible? If undoing it costs an afternoon, decide now and move; if undoing it is impossible or ruinous, slow down, check twice, and get a second set of eyes before pulling it.
- **Ambiguity:** Classification is itself sometimes wrong (the disguised one-way door is the classic catastrophe); irreversibility can be graded, and the test is the cost of the return path, not the drama of the choice.
- **Directive:** Schema drops, key rotations, and public disclosures are one-way doors — full review before any of them. Everything else in this task is a two-way door: decide within the hour.

### Zero-based reasoning
- **Implied procedure:** Justify every element from current goals and current facts; inherited defaults carry zero weight; the burden falls on each existing component to re-earn its place; deletion is the default verdict for what cannot justify itself.
- **Replaces:** Assume nothing deserves to exist just because it already does: rebuild the justification for every piece from what we're trying to do now, and whatever can't argue for itself goes.
- **Ambiguity:** Finance origin (zero-based budgeting); expensive at full scope — apply to the load-bearing layer, not the office supplies; hostile to accumulated tacit knowledge if applied with a chainsaw instead of a scalpel.
- **Directive:** Zero-base the alert rules: each one re-justifies against current SLOs or dies; "it's always been there" is not a justification, and the quarterly alert-fatigue number proves why.

### The scope-adjective trap (comprehensive / holistic / end-to-end)
- **Implied procedure:** These adjectives assert completeness without a closure rule; the repair is mechanical: define the generating rule for the set, the count, and the verification that the count is satisfied; then the adjective is either earned or retracted.
- **Replaces:** "Comprehensive," "holistic," and bare "end-to-end" mean nothing checkable — replace each with: which set, defined how, totaling what, verified against what count.
- **Ambiguity:** The words feel like rigor and function as scope inflation; "end-to-end" survives with a stated path ("from webhook to ledger, every hop named"); the other two should generally be retired from directives.
- **Directive:** Strike "comprehensive" from the audit plan; replace with: the 214 endpoints from the registry list, reconciled against the route table count, delta explained.

### YAGNI / smallest viable change
- **Implied procedure:** Implement the minimum change that tests the hypothesis or closes the need; speculative generality is deferred until a present requirement demands it; every addition carries a cost line (build, test, maintain, explain).
- **Replaces:** Do the least that solves the actual problem — no framework for future problems we don't have, no abstraction for one caller — additions wait for a second concrete need.
- **Ambiguity:** Misread as sloppiness: YAGNI governs feature scope, not quality of what's built (tests and clarity are not "speculative"); the standing counterweight is that some cheap-now provisions (logging) are brutal to retrofit.
- **Directive:** Smallest viable change: add the cache header, not the CDN; measure; if the p75 stays bad, the CDN becomes a real proposal instead of a preemptive one.

## 9. Restraint, Authority & Delegation
*Source fields: jurisprudence, medicine, security governance, aviation.*

### Proportionality
- **Implied procedure:** Scale the response's intensity to the harm prevented and the values at stake: name the metric the response is proportional to; verify no materially weaker response achieves the same end; excess is itself a defect.
- **Replaces:** Match force to stakes: before the strong measure, show the weaker one was tried or ruled out on stated grounds — because overshooting is a failure mode, not a safety margin.
- **Ambiguity:** Proportionate to what? (risk, cost, harm, authority granted — must be named); law-of-armed-conflict sense is the strict ancestor; unanchored, the word launders whatever response was preferred anyway.
- **Directive:** Proportionality check on the IP block: one abusive tenant → one tenant block, 15-minute TTL; the /24 is disproportionate unless the per-tenant block demonstrably failed.

### Surgical
- **Implied procedure:** Change exactly the target and nothing else: minimal incision, maximal preservation of surrounding tissue (code, state, behavior); collateral edits are prohibited by default and each requires its own justification.
- **Replaces:** Touch only the thing that's broken — no drive-by refactors, no reformatting, no "while I'm here"; the diff shows the defect and nothing but the defect.
- **Ambiguity:** Medical metaphor implies both precision and restraint — either alone is a scalpel waved in the wrong direction; clashes with improvement culture ("while we're in there"), which must be explicitly overruled.
- **Directive:** Surgical fix only: the one predicate clause and its test. Format-only diffs, renamed variables, and adjacent cleanups all get reverted on sight.

### Judicious / parsimonious / discriminating
- **Implied procedure:** The restraint triad: judicious = weigh alternatives before acting and say what you weighed; parsimonious = spend the minimum resource that meets the need (Occam applied to action); discriminating = draw fine distinctions between cases that deserve different treatment.
- **Replaces:** Think before spending, spend the least that works, and treat different cases differently — the three together forbid both recklessness and blanket uniform responses.
- **Ambiguity:** As bare adjectives each is praise, not procedure — they steer only when the decision-trace (what was weighed, what was spent, which distinctions were drawn) is demanded as the artifact.
- **Directive:** Be judicious, parsimonious, and discriminating here — concretely: log the alternative you rejected, the resource floor you chose, and the case feature that justified different treatment.

### Mandate / prohibit / enforce / uphold / preserve
- **Implied procedure:** The enforcement pentad, each a different act: mandate = make X required (absence of X is a violation); prohibit = make X forbidden (presence of X is a violation); enforce = detect violations mechanically and apply consequences reliably; uphold = personally refuse to violate despite pressure; preserve = actively maintain an invariant against decay.
- **Replaces:** Say which kind of rule this is: required, forbidden, mechanically-checked-with-consequences, personally-guarded-under-pressure, or maintained-against-drift — each implies different infrastructure and different failure modes.
- **Ambiguity:** Casual use swaps them freely ("we mandate security" meaning none of the five); enforcement without detection is aspiration; preserve is the weakest-sounding and most operational (an invariant needing active maintenance decays the moment maintenance stops).
- **Directive:** We prohibit plaintext secrets (presence = violation, scanner enforces), mandate review on the merge path (CI enforces), and you uphold both under deadline pressure — preserve means the checks themselves get maintenance tickets, not quiet rot.

### Ask-before-act vs. act-then-report
- **Implied procedure:** Partition all available actions by reversibility and blast radius: irreversible or wide-blast actions require explicit approval first; reversible, contained actions proceed immediately with a report after; the partition is written down in advance.
- **Replaces:** Decide now which actions need permission and which need forgiveness: destructive, external, or one-way moves wait for a yes; everything else goes now and shows up in the log.
- **Ambiguity:** The partition is the policy — without it written, each action re-litigates the category mid-flight (slow) or guesses it (dangerous); "ask" has a latency cost that itself can be the failure mode in time-critical work.
- **Directive:** Ask-before-act: deletions, external sends, spending, anything one-way. Act-then-report: everything else, logged. When unsure which list an action is on, it's on the first.

### Standing authorization
- **Implied procedure:** Pre-grant specific authority within written bounds (what, where, when, how much); exercise within bounds requires no further approval; every exercise is logged; exceeding bounds is not a gray zone, it's unauthorized.
- **Replaces:** Here's what you may do without asking each time — the exact actions, the exact limits — and everything past those limits still needs a human, every time.
- **Ambiguity:** Grants erode into assumed broader permissions ("it worked last time" ≠ authority); review cadence is part of the grant, not an afterthought; the log is what makes the grant auditable rather than anecdotal.
- **Directive:** Standing authorization: restart any non-prod service, up to 3×/day, logged. Prod restarts, schema changes, and third restarts of the same service: ask.

### Ultra vires
- **Implied procedure:** Test each contemplated action against the grant of authority that empowers this work: if the action exceeds the grant's scope, it is void regardless of its merits; the correct move is to surface the need and request the authority.
- **Replaces:** Check the action is actually inside what you were empowered to do — outside that line, even a good idea is not yours to execute; report the gap instead of filling it yourself.
- **Ambiguity:** Corporate-law origin; the doctrine's force depends on the authority document being written (a charter, a task brief, an envelope); "clearly they'd want this" is the standard rationalization it exists to block.
- **Directive:** Editing the billing plan is ultra vires for this engagement: note the need in the report, request the authority, touch nothing in that subsystem.

### Fiduciary posture
- **Implied procedure:** Act strictly in the principal's interest: conflicts of interest are disclosed before acting; self-dealing is structurally excluded; discretion is exercised as the principal would exercise it with the same information, and the loyalty runs to them, not to your convenience.
- **Replaces:** You are trusted with someone else's interests: when your interests and theirs diverge, say so out loud first, and make every call the one they'd make if they stood where you stand.
- **Ambiguity:** Legal standard from trust law, applied by analogy — its content is the conflict-disclosure discipline, not the vibe of responsibility; agent self-preservation (hiding mistakes) is the commonest quiet breach.
- **Directive:** Fiduciary posture on this account: any action that advantages your own convenience over their latency budget gets disclosed before it's taken, and errors surface the moment they're suspected.

### Primum non nocere (first, do no harm)
- **Implied procedure:** Under uncertainty about an intervention's safety, order the options by harm potential; the no-action or least-invasive option is the default; the burden falls on intervention to prove itself safer than waiting.
- **Replaces:** When you're not sure whether the fix helps or hurts, the safe default is to not touch it — inaction is a choice you're allowed, and "we had to do something" is the excuse it exists to refuse.
- **Ambiguity:** Inaction also has harms (the omission trap) — the doctrine biases correctly only when intervention's harm distribution is the wider one; in incident response under a degrading system, it can rationalize fatal passivity: state which failure mode you're guarding against.
- **Directive:** On the healthy replica: first, do no harm — no restart, no config touch; the invasive options wait for the failed node's autopsy.

### Conservative bias under uncertainty
- **Implied procedure:** When evidence is split between options, choose the one whose error you can survive: prefer the reversible, the contained, the well-understood, and the maintainable; novelty carries a surcharge that must be paid down with evidence.
- **Replaces:** When you genuinely can't tell, take the choice whose worst case we've already survived — the boring, undoable, local one — and let the exotic option win only on evidence, not on enthusiasm.
- **Ambiguity:** Bias is usually an error, and here it's a policy — scope-limited to genuine uncertainty; overapplied it becomes permanent stagnation (the established option gets an unearned home-team advantage forever).
- **Directive:** Two candidate fixes, evidence split: ship the reversible local patch tonight; the architectural rewrite needs its own evidence, not our fatigue.

### Watchful waiting / active surveillance
- **Implied procedure:** Defer intervention deliberately, not negligently: define the metrics watched, their thresholds, the check cadence, and the criterion that converts waiting into acting; the waiting itself is a prescribed state with an owner.
- **Replaces:** We're not ignoring this, we're monitoring it on purpose: here's what we watch, here's the number that changes our minds, and until then, hands off.
- **Ambiguity:** Distinct from procrastination by the existence of the conversion trigger; without thresholds and cadence it's the omission trap wearing a clinical name.
- **Directive:** Watchful waiting on the index bloat: weekly measurement, act if scan latency doubles or the Friday number degrades two weeks running; otherwise, no action before Q3.

### De-escalation
- **Implied procedure:** Deliberately reduce the intensity or tempo of an interaction or process: step down force levels one rung at a time, signal the reduction explicitly, maintain the escape path for the other party, and never de-escalate past your own safety floor.
- **Replaces:** Turn the temperature down on purpose: reduce the provocation level, say you're doing it, leave them a face-saving exit — but keep your own protective floor intact the whole way down.
- **Ambiguity:** Conflict sense vs. clinical therapy sense vs. infrastructure sense (de-escalating privileges, load); in ops contexts, de-escalating load (shedding, throttling) is the systems translation; misread as capitulation by cultures that equate firmness with volume.
- **Directive:** De-escalate the incident bridge: single spokesperson, status every 15 minutes, no blame language; in parallel, de-escalate the system — shed load, throttle ingest, hold feature flags.

### Checkfire / knock it off
- **Implied procedure:** A universal, unconditional halt signal during live operations: on receipt, stop all actions immediately, preserve current state, hold position, and await further instruction; it overrides every other priority including completion.
- **Replaces:** These words end everything mid-stream: freeze, keep the state exactly as it is, don't clean up, don't explain, just stop and listen — no instruction you were following outranks them.
- **Ambiguity:** Aviation ("knock it off") and artillery (checkfire) heritages; must be agreed as a reserved phrase in advance, or it's just another message competing for attention; the freeze must include in-flight side effects (a half-sent batch stays half-sent, visibly).
- **Directive:** "Knock it off" is reserved: from the operator it means all subtasks halt, state is preserved as-is, and you report position and await instructions — even mid-transaction, especially mid-transaction.

### Least invasive first
- **Implied procedure:** Order the intervention ladder from least to most invasive; try each rung long enough to evaluate before ascending; document why the lower rung failed before taking the higher; the ladder itself is written before starting.
- **Replaces:** Start with the gentlest thing that could work: give it a fair trial, and only climb to the stronger intervention when you can say why the milder one failed.
- **Ambiguity:** Clinical heritage (therapy ladders); inverted under time pressure ("just nuke it") — appropriate exactly when the time-critical window (§15) has closed the evaluation budget; the written ladder is what survives the pressure.
- **Directive:** Least invasive first on the stuck queue: pause consumers (1 min) → drain one topic (5 min) → restart the broker (last resort, needs the second pair of eyes).

### Chesterton's fence
- **Implied procedure:** Before removing an existing structure, determine why it was erected: research its origin and the problem it solved; if the reason is unknown, the fence stays until known; removal is licensed only by understanding, never by incomprehension.
- **Replaces:** That weird rule you want to delete was put there on purpose by someone who knew something you might not: find out what before you remove it — "I don't see why it's here" is the beginning of the investigation, not the conclusion.
- **Ambiguity:** License for paralysis if every artifact becomes sacred — the doctrine demands the reason be sought energetically, not merely assumed to exist; where no reason is findable and no failure follows removal, the fence was decoration and its removal is fine.
- **Directive:** The nightly rebuild looks pointless — Chesterton it: find the ticket and the incident that created it. If the reason exists, it goes in the runbook; if it's genuinely orphaned, delete with a tombstone note.
## 10. Monitoring & Reporting
*Source fields: SRE/operations, military communications, management communication.*

### Observability vs. monitoring
- **Implied procedure:** Monitoring = pre-defined checks against known failure signatures; observability = the ability to interrogate novel states you didn't anticipate: rich telemetry, exploratory queries, causal tracing; build for questions you can't yet name.
- **Replaces:** Alerting tells us the queue is deep — that's monitoring. The three Ms of telemetry (metrics, logs, traces) that let us ask "why this specific message, why now" — that's what we're paying for when we say observable.
- **Ambiguity:** Marketing-speak collapse ("observability solution" = a dashboard product); the honest test is novel-question interrogability, not chart count.
- **Directive:** Monitoring covers the known failure modes; verify observability separately — ask a question we've never asked before (why did tenant X's webhook double-fire) and time how long the data takes to answer.

### Instrument first
- **Implied procedure:** Add measurement to the target before changing it: establish baseline distributions, then intervene; claims about effect require before-and-after on the same instrument; no instrument, no change.
- **Replaces:** Measure it before you touch it — baseline first, change second, then compare — because "it feels faster" is not a measurement, and unmeasured optimization is roulette with extra steps.
- **Ambiguity:** The act of measuring perturbs (observer overhead, Hawthorne effects); instrumentation without defined baselines collects numbers, not evidence.
- **Directive:** Instrument the handler with a latency histogram and allocation counter; capture 24h of baseline; only then apply the patch, and the PR cites both distributions.

### Sentinel metric
- **Implied procedure:** Choose a small set of leading indicators tightly coupled to user-visible health; watch them with tight thresholds; a sentinel's alarm is a page, not a dashboard color; sentinel-ness is earned by demonstrated lead time.
- **Replaces:** Pick the two or three numbers whose movement predicts real pain before users feel it — those get paging thresholds; everything else is a dashboard, and diluting the sentinels with trivia is how on-call dies.
- **Ambiguity:** Code sense of "sentinel value" (a marker like -1 or null) is unrelated; a metric without demonstrated lead time is a vanity metric wearing a pager.
- **Directive:** Sentinels: checkout success rate and payment-p99, paging thresholds; the other forty metrics live on the dashboard and are forbidden from waking anyone.

### Exception-only reporting
- **Implied procedure:** Define the expected envelope for each metric and task; report only deviations outside it, each with magnitude, cause (known or unknown), and action taken; silence means everything is inside the envelope, by construction.
- **Replaces:** Don't narrate routine success: report only what strayed from plan, how far, why, and what you did — if everything's normal, one line saying so is the whole report.
- **Ambiguity:** Requires pre-declared thresholds or "deviation" means whatever the reporter felt; silence becomes ambiguous (all-good vs. not-checked); pair with a heartbeat (§4) that proves checking happened.
- **Directive:** Exception-only status: SITREP only when a metric leaves its envelope, plus a single "all green" heartbeat line per day to prove the checks ran.

### SITREP (situation report)
- **Implied procedure:** Report on a fixed cadence in a fixed shape: current situation, actions since last report, blockers, next actions with ETAs, needs; each field answered even when the answer is "none"; brief enough to read in 30 seconds.
- **Replaces:** Every hour during this operation send the same five-part update — where we are, what we did, what's stopping us, what's next and when, what we need — so nobody has to ask.
- **Ambiguity:** Military signal heritage; the fixed shape is the value (comparable across time and readers); a SITREP that rediscovers its format each time is just an email.
- **Directive:** Hourly SITREP during the migration: SITUATION / SINCE / BLOCKERS / NEXT+ETA / NEEDS — "none" is an acceptable entry in exactly three of the five.

### BLUF (bottom line up front)
- **Implied procedure:** Lead with the conclusion or decision required; follow with the supporting facts in descending load-bearing order; the reader must be able to stop after one sentence with the correct takeaway.
- **Replaces:** Say the answer first, then the evidence — the busy reader gets the verdict in line one, and everything after it only earns its place by changing what they'd do.
- **Ambiguity:** Journalistic/military heritage; over-application flattens genuinely exploratory reporting where the point IS the reasoning; the tail must still exist — BLUF is ordering, not amputation.
- **Directive:** BLUF every incident update: first line = verdict + decision needed; timeline and evidence follow; nothing load-bearing appears after line three.

### Pyramid principle
- **Implied procedure:** Structure communication as a pyramid: the answer at the apex, then grouped supporting arguments (each mutually exclusive), then supporting detail under each; siblings at each level answer "why" or "how" for the level above.
- **Replaces:** Organize it answer-first in layers: one governing statement, the few arguments that justify it, and the evidence under each — a reader can descend exactly as deep as they need.
- **Ambiguity:** Adjacent to BLUF (single inversion) — the pyramid is the recursive structure behind it; MECE (§ below) is the grouping rule it depends on; rigid application mangles narratives that are genuinely sequential.
- **Directive:** Rebuild the proposal as a Minto pyramid: recommendation up top, three MECE arguments beneath, evidence as the base layer; if an argument doesn't support the apex, it's out.

### MECE (mutually exclusive, collectively exhaustive)
- **Implied procedure:** Partition the subject so categories don't overlap (mutually exclusive) and leave nothing out (collectively exhaustive); test each dimension by attempting to place a random item twice (fails ME) and to place it nowhere (fails CE); repair the partition, not the item.
- **Replaces:** Slice this exactly once per item, with no leftovers: no category where an item could live twice, no item with no category — the partition itself is the deliverable, and it gets tested by trying to break it.
- **Ambiguity:** McKinsey heritage; strict MECE is often impossible for natural categories (fuzzy boundaries) — the standard degrades gracefully into "low overlap, high coverage, known gaps listed"; pretending to MECE with hidden gaps is worse than admitting the fuzz.
- **Directive:** The failure taxonomy must be MECE: try to file each incident twice (fix the overlap) and to file it nowhere (fix the gap); the un-filable stragglers get a "misc — to be classified" bucket that itself gets audited monthly.

### Progressive disclosure
- **Implied procedure:** Layer the information: headline first, summary next, full detail on demand; reveal the next layer only when the consumer's behavior signals need (request, drill-down, error); each layer is complete at its own altitude.
- **Replaces:** Don't dump everything at once: headline, then summary, then details on request — each level answers the question the reader has at that moment, and nobody reads paragraph four to learn the headline.
- **Ambiguity:** UI-design origin ( wizards, tooltips); withholding known-bad news behind layers is concealment, not disclosure discipline — the headline layer must carry the verdict (BLUF interlock); lazy summarization loses the load-bearing fact at the top layer.
- **Directive:** Report in three layers: verdict line, five-line summary, full evidence appendix — the first layer must contain the decision-relevant fact, not a teaser for it.

### Grounding (establish common ground)
- **Implied procedure:** Before proceeding on mutual understanding, verify it: state what you believe the shared context to be, have the other party confirm or correct, and repair the divergence before building on it; deixis ("that file," "yesterday's issue") is expanded to referents.
- **Replaces:** Confirm we're talking about the same thing before we go further: you say back what you think the context is, I correct it, and only then do we build on top — because mis-grounded coordination compounds silently.
- **Ambiguity:** Worst polysemy trap in this lexicon (electrical, NLP, evidence-basis, Clark's communicative sense) — in directives use "establish common ground"; repair loops must be bounded or grounding becomes an interrogation.
- **Directive:** Before executing the plan, ground it: state the target, the window, and the rollback you understood; I confirm or correct; zero unexpanded pronouns past that point.

### Liveness vs. readiness
- **Implied procedure:** Report two distinct health semantics: liveness = the process is not wedged (restart is safe/useful); readiness = the process can serve usefully (route traffic to it); map each to different actions — restarting an unready-but-live process is the classic self-inflicted outage.
- **Replaces:** Separate "am I alive" from "am I useful": alive-but-useless gets pulled from rotation, not restarted; dead gets restarted, not pulled — conflating the two is how orchestras of restart loops form.
- **Ambiguity:** Kubernetes-standardized but constantly re-implemented wrong; startup probes add a third window; dependency-down must fail readiness, not liveness, or cascading restarts follow.
- **Directive:** Liveness stays green while degraded — readiness 503s and sheds load; dependency unavailability affects readiness only; a liveness probe that checks the database will destroy the fleet at 2 a.m.

### Track and trigger
- **Implied procedure:** Score the subject periodically on a defined aggregate metric; preset score bands map to preset escalations (increase monitoring, call for help, act immediately); the escalation is triggered by the score, not by someone noticing the score.
- **Replaces:** Measure the vital signs on a schedule and let the bands act: this band means watch closer, this band means escalate, this band means intervene now — the response fires on the number, not on a human's alarm.
- **Ambiguity:** Clinical origin (early-warning scores like MEWS); the automation of the trigger step is what separates it from dashboards; unvalidated bands produce automated noise or automated complacency — calibrate against outcomes.
- **Directive:** Track-and-trigger on incident health: composite of error rate, latency delta, and blast spread, scored every 10 minutes; band 3 pages the secondary on-call automatically.

### Drift detection
- **Implied procedure:** Continuously compare actual state against the declared baseline (config, schema, or data distribution); any divergence beyond tolerance raises a finding with both states shown; the baseline is versioned and the comparison is scheduled, not ad hoc.
- **Replaces:** Keep checking reality against what we declared: any gap between the config-as-committed and config-as-running gets flagged with both versions — and the same for input distributions shifting away from the training baseline.
- **Ambiguity:** Three-way fork: infrastructure config drift, model/data drift, and mean-reversion finance sense — name which; drift found without a declared-state ledger is just surprise.
- **Directive:** Nightly drift check: deployed config vs. repo, and input feature distributions vs. the launch baseline; any divergence gets a finding with both states, and config drift auto-reverts unless waived.

### Correlation ID / trace propagation
- **Implied procedure:** Assign each request a unique identifier at ingress; propagate it through every hop, log line, and side effect; any line mentioning an ID is retrievable as the request's full story; breaks in propagation are themselves defects.
- **Replaces:** Give every request one name it keeps for life, and make every system it touches write that name down — so one ID reconstructs the entire journey, across services, queues, and retries.
- **Ambiguity:** Correlation (same ID across hops) vs. causation tracing (parent/child spans) — related, different tooling; async boundaries (queues, schedulers) are where propagation silently dies.
- **Directive:** Propagate the X-Request-ID through every hop including queue consumers and cron fan-out; any log line without a propagatable ID fails review; reconstruct one full trace as the acceptance test.

### Decision-ready communication
- **Implied procedure:** Lead with the recommendation and the decision required; attach the material consequences of each option (cost, risk, reversibility); separate facts from judgment; the reader can decide from the first paragraph and audit the rest.
- **Replaces:** Every update exists so someone can decide: recommendation first, the decision you need, and the real consequences of each path — not a balanced tour of the landscape that leaves the deciding to the reader.
- **Ambiguity:** Distinct from BLUF (ordering principle — this adds the decision-and-consequences payload); can license advocacy (pair with evidential markers and the stated rejected alternative, §11).
- **Directive:** Decision-ready form for the vendor question: recommend B, decision needed by Friday, consequences of B vs. A vs. deferring in one line each, and the one fact that would change the recommendation.

## 11. Communication Pragmatics
*Source fields: linguistics, clinical communication, technical writing.*

### Disambiguate
- **Implied procedure:** Detect the readings of the ambiguous item; if context selects one, state the selection and proceed; if not, ask a pointed question whose answer selects; never proceed on a silently-chosen reading of a load-bearing ambiguity.
- **Replaces:** If it can mean two things, say which one you're taking — or ask the one question that settles it — but don't just pick a meaning and hope; ambiguity in the load-bearing parts is not a style problem.
- **Ambiguity:** The ask-vs-guess policy is itself ambiguous (when must the agent stop and ask? — §18 threshold); over-asking transfers the thinking back to the requester; scope ambiguity, reference ambiguity, and quantifier ambiguity (§17) need different repairs.
- **Directive:** Two readings of "migrate the users": (a) schema only, (b) with data. Don't choose — ask, and list what else you'll confirm while waiting.

### Contextualize
- **Implied procedure:** Supply the minimum frame a receiver needs to interpret the fact correctly: what it's about, at what scope, compared to what baseline, at what time; test the frame by asking whether the fact could be misread without it.
- **Replaces:** Give each fact enough setting to be interpreted honestly — compared to what, over what period, at what scope — because a true number in the wrong frame is a lie with citations.
- **Ambiguity:** Degenerates into background-dumping; the test is minimum sufficient frame (misreading prevention per token); distinct from ground (the fact's basis) and from narrative (storytelling).
- **Directive:** Contextualize every SLA number: which percentile, which window, which cohort — the same "99.9%" means three different products otherwise.

### Distill
- **Implied procedure:** Reduce the material while preserving its decision-relevant content: identify the decisions the reader must make, keep what changes those decisions, discard the rest; the lossy compression is deliberate and its policy is stated.
- **Replaces:** Cut it down to what changes what we do: keep the facts that alter decisions, drop everything that merely decorates them — and tell me what you dropped so the loss is auditable.
- **Ambiguity:** All distillation is lossy by design — the protection is naming what must survive (the distillation contract); drifts into omission when the decision-relevance test is skipped.
- **Directive:** Distill the 40-page RFC to one page: keep everything that changes the build decision; your header lists the sections dropped wholesale.

### Crystallize
- **Implied procedure:** Iterate the formulation until it is precise, complete at its altitude, and stable (further words change nothing); then freeze it as the canonical wording; later references reuse the frozen form verbatim.
- **Replaces:** Work the wording until it can't be misread and more editing wouldn't improve it — then lock it as the official phrasing and reuse it exactly, so we stop re-litigating the same idea in new words.
- **Ambiguity:** Overlaps canonical (§17: the chosen form among equivalents) — crystallize is the convergence process, canonical is the result; premature freezing locks in a wording nobody has stress-tested.
- **Directive:** Crystallize the incident summary: three drafts, adversarial read of each, then freeze the result as the canonical wording for all downstream reports.

### Elucidate
- **Implied procedure:** Make the obscure legible: identify what made it inaccessible (missing background, tangled reference, jargon), supply exactly that repair, and verify legibility on a naive reader.
- **Replaces:** Explain it so it actually lands: find why it's hard to get, add precisely the missing piece, and check your explanation on someone who didn't already understand.
- **Ambiguity:** **Low-medium density flag:** names the outcome, not the repair — without the diagnose-the-obstacle step it's a synonym for "explain"; the naive-reader verification is the part worth keeping.
- **Directive:** Elucidate the consensus bug: diagnose what makes it hard (the interleaving), write the repair around that obstacle, and test the writeup on someone who hasn't read the code.

### Paraphrase-back
- **Implied procedure:** Restate the received instruction or claim in your own words, including scope and constraints; divergences between original and paraphrase are the misunderstanding made visible; proceed only on confirmed match.
- **Replaces:** Say it back in your own words before acting — including what's in scope and out — because the delta between what I said and what you heard is exactly where the damage happens.
- **Ambiguity:** Read-back (§6) repeats verbatim for transmission fidelity; paraphrase-back re-expresses for comprehension fidelity — different failure detection; conversational drift can smuggle softened constraints into the paraphrase.
- **Directive:** Before the refactor, paraphrase-back the task: goal, in-scope, out-of-scope, and the two constraints you consider hardest — I correct before you type.

### Explain-it-back (Feynman / rubber-duck)
- **Implied procedure:** Force a complete simple-language explanation of the mechanism: gaps, hand-waves, and "it just does that" moments are the diagnostic output; iterate until the explanation survives a naive listener; the explaining is the test.
- **Replaces:** Explain the whole thing in plain words to someone who knows nothing — every place you wave your hands is a place you don't actually understand, and those places are the work.
- **Ambiguity:** Productivity-culture cargo cult ("explain it simply!" as a style rule) misses the point: the value is the gap detection, not the simplicity; the naive listener can be a rubber duck, but only for the explainer who is honestly hunting their own hand-waves.
- **Directive:** Rubber-duck the race condition: write the plain-language walkthrough of both threads; every "and then presumably" in your text is a todo.

### Hedge discipline
- **Implied procedure:** Attach uncertainty markers in strict proportion to evidence strength: quantify where possible ("3 of 5 replicas agree"), never hedge what was directly observed, never assert what was inferred; strip hedges that carry no information.
- **Replaces:** Match every confidence word to how much evidence you actually have: measured things get stated flat, guessed things get flagged as guesses, and decorative maybe-words get deleted because they're noise.
- **Ambiguity:** Over-hedging obscures (and evades accountability — the weasel-word pattern §17); under-hedging fabricates certainty; the calibration target is the estimative-language scale (§1), making this its communication-side twin.
- **Directive:** One hedge per claim, evidence-scaled: "p99 grew 40ms over the window (measured), likely lock contention (inferred — 2 of 3 probes agree)."

### Evidential markers
- **Implied procedure:** Tag each claim with its source mode — measured, observed, reported (by whom), inferred, assumed — at the point of assertion; untagged claims in consequential documents are defects.
- **Replaces:** Say where each statement comes from as you make it: I measured this, the docs claim that, I'm inferring this, I'm assuming this — so the reader knows which load-bearing walls are actually load-bearing.
- **Ambiguity:** Grammatical evidentiality (some languages mark this morphologically — English doesn't, so we mark lexically); reported chains lose fidelity per hop ("vendor reports that docs claim..."); overlaps but is not identical to observation/inference/assumption separation (§1 — that's the taxonomy, this is the surface marking).
- **Directive:** Every claim in the RCA gets a bracketed marker [measured]/[observed]/[reported-X]/[inferred]/[assumed]; three [assumed]s in a chain triggers a "this RCA is fiction" flag.

### Verbatim quoting discipline
- **Implied procedure:** When precision is load-bearing (errors, commands, contract clauses), reproduce exactly, marked as quotation, with source location; paraphrase is prohibited for these classes; any ellipsis or emphasis is marked.
- **Replaces:** Quote it exactly — the error string, the command, the clause — with where it came from, because "something like a null pointer error" has destroyed many afternoons; paraphrase is for concepts, artifacts stay verbatim.
- **Ambiguity:** Over-application produces unprocessable quote-walls; the rule is precision-proportional; silent normalization of quotes (smart quotes, whitespace) is the classic corruption vector.
- **Directive:** Error messages, SQL, and config lines appear only as verbatim quoted blocks with file:line; never retype them — paste.

### Level-shifting (laddering)
- **Implied procedure:** Choose the abstraction level to match the reader's decision altitude; move deliberately between levels (up: generalize to invariant; down: instantiate to example) when understanding stalls; announce the shift.
- **Replaces:** Talk at the level where they're deciding — summary for direction, detail for execution — and when communication jams, shift explicitly up to the principle or down to a concrete example rather than repeating louder.
- **Ambiguity:** Unannounced level-shifts read as topic changes; "up-levelling" is also an evasion move (retreat from a losing concrete argument into abstraction) — the announcement requirement is the honesty device.
- **Directive:** Ladder down: the invariant is "no unbounded growth" — here's the concrete input sequence that grows it; if the concrete doesn't convince, we argue the invariant, not the mood.

### Taboo (your terms)
- **Implied procedure:** When a contested word is doing hidden work in a disagreement, ban it for the discussion: all parties must express the content in unmarked language; the real disagreement typically surfaces as either dissolving or relocating.
- **Replaces:** We can't use the word "broken" anymore in this thread — describe observed vs. expected behavior instead — because the word is smuggling a conclusion the facts haven't earned.
- **Ambiguity:** Rationalist-community coinage (not the ordinary taboo); requires enforcement power in the facilitator; applied to the wrong words it becomes euphemism treadmill (§17) rather than precision.
- **Directive:** Taboo "clean" in this review: describe what the code does and what would differ in the version you'd praise; I predict half the disagreements dissolve.

### Gricean maxims (quality, quantity, relation, manner)
- **Implied procedure:** Conform each utterance to the four conversational defaults: true-and-evidenced (quality), as informative as needed and no more (quantity), relevant to the present purpose (relation), brief and orderly and unambiguous (manner); violations are read as meaningful signals, so violate only deliberately.
- **Replaces:** Four standing rules for every sentence: don't say what you can't back, give what's needed and stop, stay on the current question, and be clear and brief — and know that readers infer intent from any deviation from these defaults.
- **Ambiguity:** Descriptive linguistics (how implicature works) used here prescriptively; over-fidelity to quantity produces exhaustive dumps (violates manner); agents exploiting the maxims' expectations is exactly how misleading-but-true statements work.
- **Directive:** Check the summary against the four maxims: every claim evidenced, no fact the decision doesn't need, everything on the launch question, ordered and plain.

### Structured interrogation
- **Implied procedure:** Systematically elicit missing information before acting: enumerate the unknowns that block the task; rank by consequence; ask pointed, answerable questions one batch at a time; record answers as constraints; iterate until the blocking set is empty.
- **Replaces:** Before you build anything, extract what you're missing: list the unknowns that actually block execution, ask the specific questions whose answers unblock — not open-ended interviews, and not silent assumptions either.
- **Ambiguity:** Not hostile questioning — the systematic elicitation sense (needs disambiguation from interrogation-as-accusation); the stop-and-ask threshold (§18) governs when interrogation replaces action; unbounded question batches offload the thinking to the answerer.
- **Directive:** Structured interrogation before the schema change: the blocking unknowns are retention, tenant isolation, and backfill scope — three questions, ranked, one round; answers become constraints in the plan.

## 12. Bias Countermeasures
*Source fields: cognitive psychology, behavioral economics, forecasting practice.*

### Consider the opposite
- **Implied procedure:** Generate the explicit negation of your leading conclusion; develop it seriously with its own evidence and mechanism; only then compare; the procedure is mandatory, not optional, when confidence is high.
- **Replaces:** Before you lock in, build the case that you're wrong — not a strawman version, the real one — because the surer you feel, the less likely you did this spontaneously.
- **Ambiguity:** Weaker than steelman (§3: strongest opposing case) — this only demands the negation be genuinely developed, not maximized; without the evidence step it's a mental nod, not a countermeasure.
- **Directive:** You're 90% on the config theory: consider the opposite — write the three best facts supporting "not config," then re-score.

### Outside view / reference class
- **Implied procedure:** Locate the case in a class of similar prior cases; take the class's base-rate outcome as the starting estimate; adjust from the reference only with case-specific evidence explicitly argued; the inside view (our story, our details) is the second opinion, not the first.
- **Replaces:** Before trusting our unique story about this project, ask how long projects like this actually took and how often they actually shipped — our details are the adjustment to that number, not a replacement for it.
- **Ambiguity:** Reference-class choice is the loaded decision (too broad dilutes, too narrow is the inside view again); planning fallacy is the named failure this corrects; the outside view offends every team that believes in its specialness.
- **Directive:** Outside view first: vendor integrations of this API class took 2–4 weeks median in our last six; our 3-day plan needs case-specific evidence line by line, and "we're different" isn't evidence.

### Base rate first
- **Implied procedure:** Before evaluating the specific evidence, establish the prior frequency of the outcome in the relevant population; force the specific evidence to move you from that prior, not from neutrality; state the prior whenever a probability is asserted.
- **Replaces:** Start from how often this actually happens — the boring statistical answer — and make the vivid specifics earn every deviation from it; a vivid story against a 1% base rate is still probably the 99%.
- **Ambiguity:** Base-rate neglect is the failure being countered; availability's vivid cases feel like evidence and are mostly base-rate noise; unspecified populations let you shop for a flattering rate.
- **Directive:** Before diagnosing exotic causes: what fraction of past 500s in this service were upstream timeouts? Start there and justify any excursion.

### De-anchoring
- **Implied procedure:** Before exposure to a reference number (their estimate, a round figure, a prior quote), derive your own independently and write it down; compare only after both exist; treat post-anchor adjustments as suspect.
- **Replaces:** Write your estimate down before you see theirs — any number you meet first drags every later thought toward it, so the only defense is committing to yours while it's still uncontaminated.
- **Ambiguity:** Anchoring survives even when the anchor is known-irrelevant (the mechanism is not reasoning); written pre-commitment is the only robust defense; re-anchoring happens at every new number entered into the discussion.
- **Directive:** Independent estimates first, in writing, before the vendor's number enters the channel; if the reveal moves your estimate, say by how much and why.

### Sunk-cost immunity
- **Implied procedure:** Evaluate every continuation decision on future costs and future benefits only: past investment appears nowhere in the calculation; explicitly strike "but we've already spent—" from deliberation; the already-spent is recoverable only via the option's own future value.
- **Replaces:** What we've put in so far is gone and irrelevant: judge only whether finishing from here beats abandoning from here — the two days of work don't vote, and neither does the embarrassment.
- **Ambiguity:** The opposite error (over-eager restarting — "restart bias") discards genuinely viable work; reputational costs are real future costs (not sunk) and belong in the calculation; escalation-of-commitment is the pathological cluster this guards.
- **Directive:** Migration is 70% done and failing: sunk-cost immunity — compare only "finish cost + risk" vs. "abandon cost + risk." The 70% is not an argument; write both columns.

### Goodhart awareness
- **Implied procedure:** For every metric driving behavior, distinguish it from the goal it proxies; predict how the measured party will game the proxy once it becomes a target; install a second, unannounced or goal-direct measure to catch divergence.
- **Replaces:** The moment this number becomes the target, someone will optimize the number instead of the goal — so say what the goal is beyond the metric, and keep a way to check the goal directly.
- **Ambiguity:** The law is usually misquoted as "metrics are bad" — the content is proxy-vs-goal divergence under optimization pressure; detection requires a measure the optimizer doesn't see or can't reach.
- **Directive:** Ticket-closure rate is a proxy: audit 5% of closures monthly against the actual-fixed criterion — that audit is the Goodhart tripwire, and its findings change the incentive, not just the report.

### Cobra effect (perverse incentives)
- **Implied procedure:** Before deploying an incentive, simulate the strategic response of the incentivized: enumerate profitable behaviors that technically satisfy the reward while harming the intent; redesign until no such behavior is the cheapest strategy.
- **Replaces:** Model the people as strategic: what's the laziest way to hit this number while defeating its purpose? Whatever you find, they will find faster — fix the incentive until that answer dies.
- **Ambiguity:** Colonial-era anecdote (bounties bred cobra breeding) standing for a general law; applies to agents as much as people — reward hacking is the ML-named sibling; attribution of specific perverse outcomes is often contested after the fact.
- **Directive:** Before we pay per migrated customer, red-team the incentive: what's the cheapest technically-compliant but worthless migration? Close that path first.

### Survivorship check
- **Implied procedure:** Ask what population the sample excludes and why: how were failures, dropouts, and non-runners filtered before the data arrived; reconstruct or at least bound the missing class before drawing comparative conclusions.
- **Replaces:** Who's missing from this dataset because they failed, quit, or were never captured? The winners' statistics describe winning, not the process — until the missing are counted, every conclusion is biased upward.
- **Ambiguity:** Selection-effect umbrella (survivorship is its most seductive member); "we only see the alerts that fired" is the ops translation; silent attrition in pipelines is the systems translation.
- **Directive:** The corpus contains only successful runs — survivorship check: pull the rejected and crashed jobs too, or say "of runs that completed" in every claim.

### Availability check
- **Implied procedure:** Before weighting a scenario, ask whether its salience comes from recency, vividness, or repetition rather than frequency; retrieve the actual frequency; discount the vivid accordingly.
- **Replaces:** Is this scenario likely, or just recent, dramatic, and much-discussed? Check how often it actually happens before letting the memorable one set the budget.
- **Ambiguity:** Availability is sometimes right (recent local events do update frequencies legitimately — the check is whether the vividness tracks the base rate, § above); news cycles are availability attacks on judgment.
- **Directive:** The multi-region outage from last week is vivid, not frequent: pull the five-year rate of that class before we redesign failover around it.

### Normalization-of-deviance guard
- **Implied procedure:** Treat every anomaly as novel until formally dispositioned: compare each deviation against the last one (count, interval, severity); repeated unexplained deviations trigger escalation and investigation, never silent re-baselining; acceptance of a deviation is a recorded decision with an owner.
- **Replaces:** The third timeout this week is not the new normal — it's a signal we've started ignoring: count the deviations, notice the trend, and make accepting any of them an explicit written decision instead of an accretion.
- **Ambiguity:** Aerospace-safety origin (Challenger o-rings); baseline drift (genuine legitimate re-baselining) vs. deviance normalization (unexamined creep) is the discriminating question; the guard is the ledger, not the suspicion.
- **Directive:** Deviation ledger on the nightly job: every anomaly logged with count-to-date; three unexplained repeats auto-open an investigation — "it usually does that" is banned as a closure reason.

### Reversal test
- **Implied procedure:** When endorsing a status quo asymmetry, test it in both directions: if the current level were lower, would you argue to raise it to here? If not, your preference is status quo bias wearing a reason; the burden falls on the asymmetry's justification.
- **Replaces:** You want to keep it at 7 — would you argue to move it to 7 if it were at 5? If you'd leave it at 5 instead, you don't have a reason, you have inertia; give the inertia a justification or drop it.
- **Ambiguity:** Rationalist formulation of status-quo-bias detection; legitimate status quo preferences pass the test (the asymmetry is justified by stated consequences); adjacent to Chesterton (§9) which guards artifacts' original reasons, not preference symmetry.
- **Directive:** We tolerate 500ms p95 "for stability": reversal test — if it were 200ms, would we argue up to 500? If not, stability isn't the real reason; find it.

### Hanlon's razor
- **Implied procedure:** Attribute harmful outcomes to incompetence, error, or misconfiguration before malice as the working prior; investigate the incompetence hypothesis first (cheaper to verify); upgrade to intent only on evidence of intent.
- **Replaces:** Before assuming this was an attack or sabotage, exhaust the boring explanations — fat-fingered config, stale cache, misunderstood runbook — and move to malice only when the evidence specifically points there.
- **Ambiguity:** It's a heuristic prior, not a moral law (malice exists, and sophisticated adversaries exploit the presumption); in security it must be paired with threat modeling (§3) or it becomes a blindfold; Heinlein's counter ("never attribute to malice that which is adequately explained by stupidity" cuts both ways) reminds you both priors are cheap.
- **Directive:** Apply Hanlon first: page the on-call for the deleted bucket as probable error (check the runbook-adjacent commands), while security pulls the access logs in parallel — the parallel track is what keeps the razor honest.

## 13. Learning from Failure
*Source fields: management practice, high-reliability organizations, software postmortem culture.*

### After-action review (AAR)
- **Implied procedure:** Convene promptly after the event; answer four questions in order — what was supposed to happen, what actually happened, why the difference, what will we sustain or change; all ranks participate; output is owned actions with dates.
- **Replaces:** Right after it ends, before memories diverge: intended vs. actual vs. the cause of the gap vs. two keepers and one change — everyone in the room, actions assigned, no skipping the "intended" step.
- **Ambiguity:** Military doctrinal origin with a strict four-question format; decays into generic "retrospective" (§ below) when the four questions blur; the intended/actual pair is what makes it evidential rather than atmospheric.
- **Directive:** AAR within 48h of the launch: the four questions verbatim, participation from every role, and every "change" answer leaves with a name and a date or it didn't happen.

### Blameless postmortem
- **Implied procedure:** Analyze the failure as a property of the system: reconstruct the timeline, identify the conditions that made each local action reasonable at the time, find the systemic causes; individual fault-finding is out of scope and out of the document; action items target systems and process.
- **Replaces:** Nobody gets named as the cause: the person who clicked the button was acting reasonably given what they could see — find what made that the reasonable move, and fix the conditions, or the same click happens with a different finger next quarter.
- **Ambiguity:** Blameless ≠ consequenceless (individual performance issues exist, handled elsewhere — conflating the two is how the practice dies); "action items" without owners and dates is the ritualized decay; psychological safety is a precondition, not a byproduct.
- **Directive:** Postmortem is blameless by charter: no names as causes, every local action explained by its visible context, action items systemic with owners — HR-shaped issues, if any, leave through their own door.

### Five whys
- **Implied procedure:** From the symptom, ask "why" iteratively — each answer becomes the next question's subject — until the cause is a process or system property rather than a person or a moment; stop when the answer would have prevented the class, not just the instance; verify the chain by walking it backward.
- **Replaces:** Keep asking why until you hit a process failure — five is a heuristic, not a quota — and if the answer at any level is a person's name, you've stopped one level early.
- **Ambiguity:** Toyota-origin; naive linear application on multi-cause failures produces a single-chain fiction (pair with causal-stack thinking below); "why" interrogates events, not people, or it becomes an interrogation.
- **Directive:** Five-whys the missed alarm: symptom → trigger absent → threshold set by guess → no calibration step → process gap. Fix the process gap; verify the chain by walking it backward to the symptom.

### Root cause analysis (RCA)
- **Implied procedure:** Systematically trace the causal chain from symptom to origin: collect evidence before it decays, reconstruct the timeline, test candidate causes with counterfactuals (but-for), distinguish triggering cause from enabling conditions, and name the systemic fix that prevents the class.
- **Replaces:** Don't patch the symptom and move on: reconstruct what actually happened, test each candidate cause against the evidence (would removing it have prevented this?), and fix the level where recurrence is actually blocked.
- **Ambiguity:** "The root cause" singular is the practice's own recurring bug — failures are stacks (§ below); RCA theater names a proximate trigger and closes the ticket; the counterfactual test is what separates analysis from narrative.
- **Directive:** Full RCA on the outage: evidence preserved first, timeline second, but-for tests on each candidate third — and the deliverable names both the trigger and the enabling conditions, or it comes back.

### Root cause vs. contributing factors (the causal stack)
- **Implied procedure:** Model the failure as a stack: the trigger (the match), the enabling conditions (the dry forest), and the absent safeguards (the missing firebreak); remediation addresses each layer it wants to keep; any single-layer story is flagged as incomplete.
- **Replaces:** The deploy didn't cause the outage alone: it was the trigger. The stale failover config and the unmonitored queue were the fuel. Write the stack — trigger, conditions, missing safeguards — and fix at the layers you choose to keep.
- **Ambiguity:** Legal causation doctrine (proximate cause) pulls toward the single culpable event; Swiss-cheese framing (§ below) is the same model in defense-layer clothing; "contributing factor" lists without assignment of which layer gets the fix are decoration.
- **Directive:** Causal stack for the incident: trigger (config push), enablers (cache TTL, silent queue growth), absent safeguards (no I&W on depth) — the remediation PR must touch at least two layers.

### Swiss cheese model
- **Implied procedure:** Model defenses as layered slices each with holes (active failures and latent conditions); harm passes only when holes align across all layers; analysis asks which holes aligned, and hardening asks which layer's holes to shrink or shuffle — not which single hole "caused" it.
- **Replaces:** Every safeguard has gaps, and the disaster happened because the gaps lined up that day: map the alignment, then shrink or de-synchronize the holes in the cheapest layers — no single hole is the culprit.
- **Ambiguity:** Aviation-medicine origin (Reason); the model explains pass-through, not why each hole existed (that's the RCA's job); static hole-thinking misses that holes drift (§12 normalization of deviance).
- **Directive:** Swiss-cheese the leak: reviewer gap + scanner exclusion + shared credential aligned across the three layers — the fix shuffles at least one layer, not just patches the reviewer.

### Double-loop learning
- **Implied procedure:** First loop: correct errors against current goals and norms. Second loop: question the goals and norms themselves in light of the error; when single-loop fixes keep recurring, the defect is in the governing variables, and the second loop is mandatory.
- **Replaces:** Beyond fixing the mistake against today's rules — ask whether today's rules produced the mistake: if this same class of fix keeps coming back, the goals or assumptions themselves are the thing to change.
- **Ambiguity:** Management-theory coinage (Argyris); double-loop on everything is thrash — the trigger is recurring single-loop fixes; easily invoked as an excuse to relitigate settled strategy after every stumble.
- **Directive:** Third queue-overflow fix this quarter: double-loop it — the governing assumption (unbounded ingest is fine) is now on the table along with the patch.

### Error budget
- **Implied procedure:** Derive the sanctioned unreliability from the SLO (e.g., 99.9% ⇒ 43 min/month); burn it consciously, tracking the burn rate; when the budget exhausts, feature work halts in favor of reliability work until rebuilt — the halt is the mechanism, the budget is the currency.
- **Replaces:** Reliability has a price and we've agreed to pay it in error-minutes: spend them knowingly, watch the burn rate, and when you've spent them all, new features stop until the account refills.
- **Ambiguity:** SRE heritage (Google); the policy's force is entirely in the enforced feature-freeze (without it, it's a dashboard); budget arithmetic is a governance device, not an engineering truth about acceptable harm.
- **Directive:** The migration burned 30% of the quarter's error budget in a night: feature freezes per policy until we're back under 15% — the freeze is automatic, not a meeting outcome.

### Dogfooding
- **Implied procedure:** Consume your own output under real conditions: the team uses the product as primary, in production, with real stakes; defects surface through lived pain rather than synthetic reports; complaints route through the same channels as customers'.
- **Replaces:** Use it yourself, for real, as your only option — eat what you cook — because the bugs you'll tolerate as a spectator you'll fix as a victim.
- **Ambiguity:** Team-unrepresentativeness (power users forgiving expert-hostile UX) limits the evidence value; mandated dogfooding without escape-valve reporting becomes suffering theater; distinct from beta (external users, informed consent).
- **Directive:** The CLI ships when the platform team has run on it exclusively for two weeks; every workaround we caught ourselves performing is a filed issue, not a habit.

### Deliberate practice
- **Implied procedure:** Practice at the edge of current ability on specific subskills, with immediate feedback and repetition with variation; comfort-zone repetition doesn't count; the practice loop includes a coach or criterion that catches drift.
- **Replaces:** Repeating what you're already good at isn't practice: isolate the weak subskill, drill it just past comfortable, get told immediately what was wrong, and vary it until it generalizes.
- **Ambiguity:** Expertise-research coinage (Ericsson) now diluted to "practice deliberately, you know, with effort"; for agents: fine-tune on the failure distribution, not the easy pass set — the training-set selection is the practice design.
- **Directive:** Deliberate practice on incident comms: drill only the degraded-channel scenario we historically fumble, with scored feedback each round and one varied complication per iteration.

### Calibration training
- **Implied procedure:** Make predictions with explicit confidence; record them; score against outcomes (Brier-style); adjust confidence-mapping from the scored history; repeat until stated confidence matches hit rate across the range.
- **Replaces:** Say how sure you are in numbers, keep the receipts, and grade yourself later — over time your 80%s should be right 80% of the time, and the only way to get there is scored practice, not introspection.
- **Ambiguity:** Forecasting-practice heritage (superforecasters, Tetlock); calibration is domain-specific (80% on your own code ≠ 80% on vendor timelines); the estimative-language scale (§1) is where calibrated confidence gets expressed.
- **Directive:** Every go/no-go recommendation this quarter carries a number and lands in the calibration ledger; monthly, we plot stated-vs-actual and adjust the mapping.

### Institutionalized lessons
- **Implied procedure:** Convert each learned lesson into a structural carrier — a test, an alert threshold, a checklist line, a lint rule, a doc section — within the same cycle; lessons existing only in narrative form are counted as lost; the conversion rate is itself tracked.
- **Replaces:** A lesson that isn't a test, an alert, a checklist line, or a gate didn't happen: put the learning into a structure that enforces it, this sprint — or admit we're keeping it as a story we enjoy retelling.
- **Ambiguity:** Military lessons-learned processes can drown in mandatory paperwork (the ritual outliving the learning); structures rot without owners — the maintenance ticket (preserve, §9) is part of the conversion.
- **Directive:** Every postmortem action item lands as one of: test / alert / checklist line / lint rule / doc section — owner and carrier named at creation; quarterly report shows conversion rate and rot rate.
## 14. Negotiation & Incentive Awareness
*Source fields: negotiation theory, economics, principal-agent theory.*

### BATNA (best alternative to a negotiated agreement)
- **Implied procedure:** Before negotiating, identify what you will actually do absent agreement; cost it concretely; improve it if cheap; treat it as the floor — no agreement worse than the BATNA is accepted, by rule rather than mood.
- **Replaces:** Work out your real walk-out option before the call and what it costs us — that alternative, not our hopes, is the floor under every term we discuss.
- **Ambiguity:** Distinct from the stated "bottom line" (a number you declare) — BATNA is the real alternative; estimating the counterparty's BATNA is the same discipline mirrored.
- **Directive:** Compute our BATNA before the vendor call: self-host, three weeks, $40k — anything worse than that on paper gets declined without a meeting.

### Walk-away point
- **Implied procedure:** Pre-commit the minimum acceptable terms while calm; when breached, terminate rather than continue; the commitment is binding under the pressure of the moment, by prior arrangement.
- **Replaces:** Decide now the worst terms you'll accept — because in the room you'll rationalize anything — and when the offer crosses that line, you leave; the decision was made last week.
- **Ambiguity:** Set-during-the-session walk-aways are anchored to whatever is on the table (§12); hidden vs. disclosed reservation points are different strategies; a walk-away you override once becomes advisory forever.
- **Directive:** Walk-away is 72-hour SLA or we cancel: state it once, act on it mechanically, no renegotiation with ourselves in the hallway.

### ZOPA (zone of possible agreement)
- **Implied procedure:** Estimate both parties' reservation points; the interval between them is where any deal can exist; no overlap means no deal is reachable at any skill level — change a reservation point or leave, don't negotiate.
- **Replaces:** Map their floor against our ceiling before investing weeks: if those numbers don't overlap, the talks are theater — improve an alternative or walk, no amount of charisma closes a ZOPA that isn't there.
- **Ambiguity:** Estimates, not observations — reservation points hide (§ information asymmetry below); the ZOPA shrinks and moves as both sides learn.
- **Directive:** Their floor is ~$8/user, our ceiling $12: a ZOPA exists — anchor inside it, don't waste rounds outside.

### Interests vs. positions
- **Implied procedure:** For each stated demand, elicit the underlying need it serves; negotiate over needs, not formulations; generate options that satisfy the interest through a different position; incompatible positions frequently conceal compatible interests.
- **Replaces:** "No deploys on Friday" is a position — the interest is incident coverage when staffing is thin: solve for coverage and several designs appear that the Friday-ban never would.
- **Ambiguity:** Requires disclosure the other side may resist (their interest is leverage); agent-relevant in requirement disputes: the stated spec is a position, the constraint behind it is the interest.
- **Directive:** Before countering the "no Friday deploys" rule, extract the interest: if it's on-call coverage, propose the coverage roster and keep the deploys.

### Salami tactics (detect)
- **Implied procedure:** Recognize incremental advances that would be rejected as a whole: each slice is calibrated too small to fight; counter by naming the pattern, re-aggregating the slices into the rejected whole, and pricing the sequence, not the step.
- **Replaces:** Watch for slice-by-slice creep: any single concession is trivial, but the sequence ends somewhere you'd have refused in one ask — evaluate the destination, not today's sliver.
- **Ambiguity:** The detection is retrospective (the pattern exists after 2–3 slices); legitimate incrementalism (staged rollouts, escalation ladders) shares the form — the discriminator is whether the whole was ever presented and declined.
- **Directive:** Third "small extension" to the data-sharing scope this month: call it salami — re-open the aggregate scope for decision, not the delta.

### Nibble (detect)
- **Implied procedure:** Recognize last-minute small additions after agreement is reached; treat any reopening as reopening the whole; decline by standing rule or the entire package returns to the table.
- **Replaces:** The tiny "one more thing" after yes is a tested exploit: either it's a flat no, or everything is back on the table — absorbing it with a smile trains its repetition.
- **Ambiguity:** Politeness norms make refusal socially expensive (the exploit's engine); distinguish the nibble from genuinely discovered scope (which goes through re-scoping, §8, at full ceremony).
- **Directive:** Contract is signed; the "just add SSO for two admins" request is a nibble — it enters the change process with its own price, not the pen.

### Skin in the game
- **Implied procedure:** Expose decision-makers to the downside of their decisions structurally (on-call rotation, deferred compensation, shared budget); discount advice from parties immune to consequences by default; design arrangements so downside travels with the choice.
- **Replaces:** Whoever proposes must also absorb some of the pain if it's wrong — recommendations from the consequence-immune get discounted automatically, not argued with.
- **Ambiguity:** Taleb-popularized; the structural exposure is the content, not the rhetoric of accountability; agent-translation: an agent that can't bear downside must route its one-way recommendations through someone who can.
- **Directive:** The proposing team carries on-call for the change's first month — that clause is what makes the proposal a proposal instead of a wish.

### Principal-agent audit
- **Implied procedure:** Map each delegation link: whose goal, who executes, how the executor is actually rewarded; the divergences are where reported information gets gamed; verify outcomes at the goal level, not reports at the activity level.
- **Replaces:** At every "X works for Y" layer, ask what X actually optimizes and how X is paid — then check Y's goal directly at the outcome, because the status report was written by X's incentives.
- **Ambiguity:** Requires an actual incentive map, not cynicism; applies to tools and agents as much as people (a review-bot optimized for throughput approves everything); moral-hazard framing is the risk-side sibling.
- **Directive:** Principal-agent check on the outsourced QA: they're paid per closed ticket — audit a sample of closures against the defect-reopened rate before trusting the 98% pass figure.

### Information asymmetry (signaling / screening)
- **Implied procedure:** Recognize when one party knows more; to learn the informed side's type, either design signals (costly to fake) or screens (choices where each type's honest answer is their cheapest move); never extract truth by asking alone.
- **Replaces:** They know things we don't, and they'll say whatever helps: set up choices where telling the truth is each type's cheapest strategy — the structure reveals what the interview won't.
- **Ambiguity:** Economics-formal (Akerlof/Spence) but operationally real in vendor selection, hiring, and agent self-reporting (an agent's confidence claim is cheap talk — demand a costly signal like a reproducible artifact).
- **Directive:** We can't verify their uptime claims by asking: offer two contract shapes (penalty-backed vs. flat) — the choice screens the ones who believe their own SLA.

## 15. Clinical Reasoning & Triage
*Source fields: medicine, emergency response.*

### Triage
- **Implied procedure:** Under scarcity, sort items by the protocol's key (urgency × salvageability × resource cost); apply the ordering rule, not the worst-first reflex; re-sort as states change; categories the protocol assigns to deferred care are honored as decisions.
- **Replaces:** You cannot do everything now: rank by what the protocol says — urgent and savable with available effort first, not the loudest or the sickest alone — and re-rank whenever anything's state changes.
- **Ambiguity:** Commonly misread as "worst-first"; different protocols order differently (treatable-first maximizes survivors — mass-casualty logic inverts the ICU's); clinical triage licenses deliberate non-treatment of some categories, which ports to task management only with care.
- **Directive:** Triage the backlog by sev × recoverable × effort; re-triage every two hours; rescoped items re-enter the sort — they don't keep their old rank by tenure.

### Resuscitate before diagnosing
- **Implied procedure:** Stabilize first: stop active damage, restore vital functions, then investigate cause; diagnosis proceeds on the stabilized system; some evidence loss to stabilization is accepted by doctrine.
- **Replaces:** Stop the bleeding before asking what caused it: cap the queue, shed load, freeze deploys — the autopsy happens after the patient has a pulse.
- **Ambiguity:** Stabilization destroys some forensic state (restarts clear memory) — snapshot first when it's cheap (§7); the doctrine orders stabilization over explanation, not over evidence preservation when both are possible.
- **Directive:** Site is down: rollback both deploys now, throttle ingest, snapshot the heap — root-cause work starts once error rate is flat, not before.

### Differential diagnosis
- **Implied procedure:** Generate at least two competing explanations; list the features that discriminate among them; order tests by information gained; act provisionally on the leader while testing; revise on results; a single-hypothesis conclusion without rivals considered is a defect.
- **Replaces:** List the plausible causes, note which observation would look different under each, test for those differences, treat the front-runner meanwhile, and switch when the results say so — a cause reached without considering its rivals is a guess in a lab coat.
- **Ambiguity:** Hickam's counterweight applies (§2): multiple simultaneous causes are the norm in complex systems; in agent use the deliverable is the rivals list — "most likely cause" with no runner-up stated is the failure signature.
- **Directive:** Differential for the p99 spike: lock contention vs. allocator pressure vs. downstream slow-ramp — one discriminating measurement per hypothesis, ordered by what each would rule out.

### Red-flag screening
- **Implied procedure:** Maintain the predefined marker list for must-escalate conditions; screen every case cheaply and early against it; any flag routes to the escalation path immediately, independent of the assessor's overall severity judgment.
- **Replaces:** Check every case against the known danger signs before anything else: one flag means the escalation path fires, even if the case otherwise looks mild — the list outranks your gestalt.
- **Ambiguity:** Depends on the list's maintenance (flags rot: both false-alarm fatigue and missing new flags); the screen is cheap by design so it can run on everything; distinct from sentinel metric (§10) — that watches populations, this screens cases.
- **Directive:** Every intake passes the red-flag list first: PII in logs, unbounded query, cross-tenant read — any hit pages the security rota before triage continues.

### Empiric then targeted
- **Implied procedure:** When evidence is pending and stakes are time-bound: act broadly to cover the likely spectrum, explicitly marked provisional; narrow on arriving evidence; the broad action has a scheduled replacement by the targeted one.
- **Replaces:** Cover all the likely causes now, narrow when the results arrive — the broad move is a bridge with an expiry date, not a conclusion, and "narrow later" is on the calendar.
- **Ambiguity:** Broad action carries breadth costs (side effects, blast radius §5) that must be priced; sepsis protocol is the reference; the ops translation is rollback-everything-then-bisect.
- **Directive:** Empiric first: freeze both suspects' features, restore p99, then bisect to the culprit and un-freeze the innocent one — the freeze has a 48-hour review date.

### Therapy de-escalation
- **Implied procedure:** Once cause is established, deliberately withdraw the broad measures instituted empirically; verify stability on the narrower regime; each leftover emergency measure is tracked as an open defect.
- **Replaces:** Now that we know it was the config, undo the emergency blocks and reroutes we sprayed at everything — every leftover emergency measure is a small standing outage with our name on it.
- **Ambiguity:** De-escalation fear (withdrawal = risk of recurrence) leaves forensic scaffolding in production for years; requires the verification step or it's just forgetting in reverse.
- **Directive:** Cause confirmed: schedule withdrawal of all four emergency mitigations one per day, each with its own stability check — "temporary" is not a lifecycle.

### Contraindication check
- **Implied procedure:** Before applying the standard remedy, screen the case against the conditions under which it is harmful; the list is consulted every time, from the document, never from memory; any hit redirects to the alternative protocol.
- **Replaces:** Check the never-do-this list before the usual fix: the standard remedy is actively harmful under some conditions, and those conditions get looked up each time, not recalled.
- **Ambiguity:** Pharmacological heritage; the memory-consultation failure is the point (memorized lists decay — §13 normalization); conflated with side effects (unavoidable costs) — contraindications are conditional prohibitions.
- **Directive:** Before "restart the worker" as first-line: check contraindications — in-flight batch > 10k or replica count < 2 → use the drain-then-restart protocol instead.

### Interaction check
- **Implied procedure:** Enumerate all co-present interventions and conditions; check each new addition pairwise against them for harmful interaction; the check re-runs at every addition, not only at baseline.
- **Replaces:** This fix doesn't act alone: check it against the three mitigations already running, pairwise, every time we add anything — drug-interaction logic for operational state.
- **Ambiguity:** Pairwise checking misses three-way interactions (known limitation, state it); drift makes the "currently running" list unreliable without a registry (§10 drift detection interlock).
- **Directive:** Adding the retry-with-backoff? Interaction check: with the circuit breaker's cooldown, retry amplifies 503s to a storm — adjust one or the other, on paper, before merge.

### Time-critical window
- **Implied procedure:** Identify the interval within which action changes the outcome; inside it, act on partial information (empiric mode); past it, priorities re-rank — investigation and harm-limitation over intervention; the window's edges are stated, not felt.
- **Replaces:** There's a period where doing something beats knowing everything, and a moment after which it doesn't: name both edges now — inside, act dirty; outside, diagnose clean.
- **Ambiguity:** "Golden hour" heritage oversimplifies graded windows; acting-inside-the-window licenses lower evidence standards, which must revert after it closes (empiric-then-targeted interlock).
- **Directive:** Rollback window is 90 minutes post-deploy (schema still compatible): inside it, rollback on abort criteria without asking; after it, we're in investigate-and-migrate-forward territory.

### Escalation ladder
- **Implied procedure:** Predefine the ordered sequence of increasingly strong interventions; each rung has entry criteria, a dwell time, and an exit check; skipping rungs is a recorded decision; de-escalation descends rung by rung with the same ceremony.
- **Replaces:** Write the ladder from gentle to drastic with each rung's trigger: climb one rung at a time unless you log why you jumped — and coming down gets the same discipline as going up.
- **Ambiguity:** Ladders lock in monotonicity assumptions (some situations need rung 3 then rung 1); dwell times are guesses until calibrated (§13); distinguish from escalation control (§16: initiative over the ladder vs. the ladder itself).
- **Directive:** Cache invalidation ladder: single key → prefix → full flush, each with entry criteria and a 5-minute effect check; the full flush requires a second approver, logged.

### Never event
- **Implied procedure:** Designate the zero-tolerance error class; any occurrence halts related work for immediate structural remediation and formal report; prevention is engineered (interlocks, §4), never vigilance-based; "be more careful" is not a closure.
- **Replaces:** Some mistakes we refuse to normalize: when one happens, everything stops, the enabling mechanism gets structurally removed, and the report names the mechanism — not a reminder to be careful.
- **Ambiguity:** Medical-patient-safety origin (wrong-site surgery class); over-broad designation inflates everything to Sev-1 and dilutes the class; the structural-prevention requirement is what separates it from ordinary severity language.
- **Directive:** Plaintext credentials in chat are a never event: halt, rotate, purge, and fix the sharing mechanism — the postmortem may not contain "reminded the team."

## 16. Command & Control
*Source fields: military doctrine, aviation operations.*

### Commander's intent
- **Implied procedure:** State purpose, end state, and hard constraints; delegate method; executors re-plan freely as facts change but never violate intent; when orders conflict with reality, intent arbitrates; verify internalization by scenario, not by nod.
- **Replaces:** Give the why, the finish line, and the non-negotiables — then let the executor choose the how and adapt when reality diverges from plan; when the plan breaks, the intent is the part that survives to be obeyed.
- **Ambiguity:** Intent is not license: constraints bind (goal-hacking is compliance theater aimed at intent); requires genuine internalization — the comms-die test ("what would you do if I went silent?") checks it.
- **Directive:** Task: "Zero data loss, reads restored by 18:00, CFO notified at done — method is yours. If both replicas fail, stop and report rather than improvise beyond the stated bounds."

### Mission-type orders (Auftragstaktik)
- **Implied procedure:** Specify what must be achieved and why; never prescribe how; evaluate execution by intent-compliance rather than step-compliance; the order is incomplete unless it carries intent and constraints.
- **Replaces:** State the outcome and the reasons; leave the path to the executor with the best local information — and judge the result against the intent, not against the route you'd have walked.
- **Ambiguity:** Prussian doctrine whose price is executor competence and shared doctrine (without both it decays into negligence with a German name); boundaries (ROE, § below) remain binding under method-freedom; misread as "no reporting."
- **Directive:** Order: "Staging green by Thursday because the demo gates on it." How is yours; daily SITREP still required; the ROE on prod still applies.

### OODA loop
- **Implied procedure:** Cycle observe→orient→decide→act at a tempo that keeps your picture fresher than the situation's drift; invest in the orient step (models, priors, assumptions) — it is where the loop wins or amplifies error; detect when your models, not the world, are the lag.
- **Replaces:** Keep cycling: see, update your mental model, decide, act — faster than things change — and notice that the model-updating step is the whole game: fast loops with stale models are error at tempo.
- **Ambiguity:** Boyd's payload is orientation quality, but the term circulates as "be fast"; the adversary-degradation half (upsetting their loop) rarely ports to ops; orientation errors are invisible from inside the loop (pair with devil's-advocate, §3).
- **Directive:** Incident OODA cadence: observations every 5 minutes; orientation stated aloud in one line ("we now believe X because Y"); decide, act, repeat — anyone whose observation contradicts the orientation says so in-channel immediately.

### Initiative in the commander's absence
- **Implied procedure:** When guidance is unreachable or stale, act on the known intent within standing constraints; log the decision and its reasoning; report on contact resumption; inaction pending permission is itself a violation when the situation demands motion.
- **Replaces:** No answer from the operator doesn't mean stop: act as the stated intent directs within the written bounds, write down what you did and why, and surface it the moment contact returns — waiting for permission while the house burns is not patience, it's abdication.
- **Ambiguity:** Requires pre-published intent and bounds, or it's improvisation wearing a doctrine; deliberately wrong for one-way doors (§8) — the bounds must state which actions are never improvised.
- **Directive:** If the operator is unreachable past 30 minutes: proceed on stated intent within the envelope, log each decision as made, and hold all one-way actions for contact — then brief on resume.

### Rehearsal
- **Implied procedure:** Execute the plan under simulation or reduced stakes before the live event, with real timings and real handoffs; gaps found are fixed before the event; the rehearsal itself is scheduled work, not aspiration.
- **Replaces:** Run the whole thing once where mistakes are cheap: same people, same clock, same handoffs — what breaks in rehearsal gets fixed before it counts, and "we'll walk through it on the day" is the opposite of this.
- **Ambiguity:** Distinct from test (artifact-level) and drill (single motion) — rehearsal integrates humans and timing; rehearsals in stale environments certify nothing (§6 dry-run caveat).
- **Directive:** Full migration rehearsal Thursday on the staging copy: real runbook, real on-call rotation, wall-clock timing; every stumble becomes a runbook edit, and Friday's live run cites the rehearsal log.

### Warning order (WARNO)
- **Implied procedure:** Announce a probable task immediately with everything currently known; recipients begin all preparation that doesn't depend on missing details; follow-on orders complete the picture without re-transmitting the known.
- **Replaces:** Tell them it's probably coming, now: what, roughly when, and what's still unknown — prep work starts on the knowns, and nobody idles waiting for the full order.
- **Ambiguity:** Probable ≠ ordered — recipients must not treat a WARNO as authority for the action itself, only for preparation; without follow-through discipline it trains alert-fatigue.
- **Directive:** WARNO: 60% probability of an emergency patch window tonight 22:00–02:00 — stage the artifact, pre-verify the rollback, await the FRAGO or stand-down.

### Fragmentary order (FRAGO)
- **Implied procedure:** Issue only the delta against an established base plan: changed steps, times, constraints; everything unreferenced stands exactly as issued; receivers merge the delta onto their copy of the base.
- **Replaces:** The plan stands except for this: report only what changed — don't re-broadcast the whole document for thoroughness, and don't silently rewrite the unchanged parts while you're at it.
- **Ambiguity:** Requires an unambiguous base-plan version (deltas against a moving base corrupt silently); "fragmentary" misread as "incomplete/sloppy" — it is precisely scoped, not lazy.
- **Directive:** FRAGO for tonight: window shifts to 23:00; shard 4 defers to next window; abort criteria unchanged. All else per ops plan v3 — merge and confirm.

### Battle rhythm
- **Implied procedure:** Publish the fixed cadence of synchronization points — reports, syncs, gates, handoffs; coordination happens on the calendar, not by interrupt; ad-hoc interrupts are reserved for abort-class events; the rhythm is visible to all participants.
- **Replaces:** Set the heartbeat: we sync at these times in this format, everything else waits for the next beat unless it's a stop-the-line — so execution is punctuated by design, not by whoever panics first.
- **Ambiguity:** Aviation/ops heritage; a rhythm without interrupt-class rules collapses back to interrupt-driven; too-dense rhythms are interrupt-driven with extra ceremony (SITREP interlock, §10).
- **Directive:** Launch-day battle rhythm: SITREP on the hour, sync at 4-hour gates, decision-brief at go/no-go; interrupts only for abort-criteria events — everything else queues for the top of the hour.

### Rules of engagement (ROE)
- **Implied procedure:** Pre-publish the action envelope: always-permitted, never-permitted, permitted-on-condition; the envelope binds regardless of situational heat; actions outside it require new authority, not in-the-moment judgment; violations are reported even when benign.
- **Replaces:** The standing list of what you may do, must not do, and may do only under stated conditions — written before contact, checked before action, and no urgency rewrites it mid-flight; wanting outside the envelope means requesting authority.
- **Ambiguity:** Military origin with legal force — borrowed sense loses the court-martial but keeps the pre-commitment logic; ROE (what's authorized) vs. abort criteria (§4: what ends the operation) are orthogonal; self-modified ROE is the classic runaway-agent signature.
- **Directive:** ROE for this run: read anywhere in the repo; write only staging; no external calls except the package registry; no deletions, no force-pushes, no secrets in output. Breach, even harmless, gets logged.

### Exploitation of success
- **Implied procedure:** When a breakthrough holds, press it immediately: reallocate resources to expand the gain before the window closes; follow-through units and rollback criteria are prepared in advance; success triggers the next phase by standing rule.
- **Replaces:** When it works, push: the fix holding on shard 1 goes to the remaining shards tonight, with the same gates — breakthroughs are for exploiting while conditions hold, not for scheduling a meeting about.
- **Ambiguity:** Military exploitation is disciplined pursuit, not triumph — the abort criteria of the expanded phase still bind; over-exploitation past evidence (canary → 100% on one green signal) is how wins become incidents.
- **Directive:** Canary is clean at 1% for 30 minutes: exploit — 5% → 25% → 100%, each rung with its own dwell and abort line; any regression halts the climb.

### Probing action
- **Implied procedure:** Commit a small, expendable test whose objective is the system's response rather than the gain; the probe is budgeted for loss; the elicited response is recorded and fed into the real plan.
- **Replaces:** Send the cheap test in first: one user, one region, one transaction — you're buying information about how the system reacts, and the probe is written off by design, win or lose.
- **Ambiguity:** Military sense (reconnaissance-in-force) vs. social sense (testing boundaries — feints and probes in manipulation share the mechanics, which is exactly why the pattern deserves recognition in inbound requests).
- **Directive:** Probe the new rate limiter with one synthetic tenant at 2× burst: record the response shape and timing; the production rollout plan is written from the probe's data.

### Left of bang
- **Implied procedure:** Place the bad event ("bang") on the timeline; identify its precursors; position detection and action upstream of the event; every post-event response gets examined for its precursor signature and converted leftward.
- **Replaces:** Put the tripwire before the explosion: alert on the curve that precedes the outage, not the outage — and for every incident we handled right of bang, find the left-of-bang signal we ignored.
- **Ambiguity:** Force-protection training coinage ("bang" = the ambush moment) — the bang must be defined per domain or the phrase decorates; precursor lead time bounds how far left is meaningful.
- **Directive:** Go left of bang on the DB pool: alert on connection-wait percentile growth, not on pool exhaustion; the last three outages each had a 20-minute visible ramp.

### Escalation control
- **Implied procedure:** Retain deliberate initiative over the intensity ladder: each raise in level is a decision with a threshold and an owner; lowering is scheduled with equal ceremony; drifting upward one incident at a time is the named failure mode.
- **Replaces:** We choose the intensity, not events: raising the level is an explicit decision with a name on it, and coming back down is also planned — because systems catch fire by escalating one "temporary" measure at a time.
- **Ambiguity:** Distinct from the ladder itself (§15) — this is initiative over it; de-escalation (§9) is its descending half; conflated with organizational escalation (paging humans).
- **Directive:** We're at mitigation-level 2 (throttled + cached): level 3 (read-only mode) requires the IC's explicit call with a threshold; scheduling the descent back to 0 is part of tonight's plan, not an afterthought.

## 17. Linguistic Precision & Framing
*Source fields: linguistics, analytic philosophy, technical writing.*

### Operational definition
- **Implied procedure:** Define each load-bearing term by the measurement procedure that instantiates it — instrument, steps, criterion; terms lacking a procedure are banned from gating claims in the document; the definitions travel with the spec.
- **Replaces:** "Slow" here means p95 > 300ms over a rolling 10 minutes measured at the edge — every term that gates behavior gets defined as a procedure, and a term we can't define that way doesn't gate anything.
- **Ambiguity:** Bridgman's operationalism applied to specs; over-application produces pseudo-precision for genuinely qualitative terms; definitions must version with the spec (§10 drift interlock).
- **Directive:** Rewrite the SLO doc with operational definitions: every threshold term states instrument, window, and aggregation — anything undefined becomes a TODO, not a gate.

### Quantifier-scope pinning
- **Implied procedure:** For each "each/every/some/one" claim, state the binding order explicitly (for-all-X-exists-Y vs. exists-Y-for-all-X); scope-silent specifications are rejected; the two readings often produce different systems.
- **Replaces:** "A token per user" or "one global token for everyone"? Pin the binding order in writing — the two English sentences are near-identical and the two architectures are incompatible.
- **Ambiguity:** Natural language under-specifies scope by default (logic's ∀/∃ discipline is the repair); garden-path sentences exploit the same looseness; agents implementing from prose inherit the ambiguity wholesale.
- **Directive:** Spec line "one connection per shard" is scope-ambiguous: pin it — ∀shard ∃connection (per-shard pools) or ∃connection ∀shard (shared client) — and the PR cites which.

### Nominalization unpacking
- **Implied procedure:** Convert event-nouns back into actor + action + object: "validation failed" → "the validator rejected the schema at line 4 because the enum lacks 'pending'"; noun-stacks that hide agency are rewritten on sight.
- **Replaces:** Turn the abstract noun back into who-did-what-to-whom: "the migration's failure" becomes "the migrator skipped step 3 because the flag defaulted to false" — if you can't name the actor and the action, the sentence isn't saying anything yet.
- **Ambiguity:** Style-guide heritage (plain-language movements); nominalization is legitimate for stable concepts — the target is agency-hiding event-nouns in incident and spec prose.
- **Directive:** Incident summary pass: every "-tion" noun gets unpacked to actor+action or deleted; "the corruption occurred" is banned in favor of "the writer appended partial records after the crash."

### Performative utterance
- **Implied procedure:** Mark commitment-performing statements explicitly and attributably ("I approve," "we accept," "I resign"); saying it on the record is the act; validity conditions — authority, receipt, timestamp — are verified as part of the act.
- **Replaces:** Approvals and acceptances happen as explicit, attributable, timestamped speech acts — not implied between the lines of a longer message where they deniably didn't happen.
- **Ambiguity:** Austin's speech-act theory origin; implicit performatives ("this is approved") weaken attribution — explicit first-person forms carry the accountability; template spam makes "I approve" cheap again (pair with two-person rule, §5).
- **Directive:** Approvals are performatives: the PR merges on a comment of the exact form "I approve merge of PR #N" from a listed reviewer — reactions, emojis, and silence don't count.

### Loaded language (detect)
- **Implied procedure:** Flag terms whose affective packaging smuggles an evaluation; re-express the content in neutral descriptors; the smuggled verdict is then argued on evidence or withdrawn; both flattering and derogatory loads count.
- **Replaces:** "Careless deploy" smuggles a verdict into the timeline: rewrite as "deploy ran without the staging gate" — facts carry the report, and verdicts ride separately with their own evidence.
- **Ambiguity:** Complete neutrality is neither possible nor the goal (framing is inescapable — the procedure is making the frame visible); loaded ≠ technical (precise terms with negative prosody, like "leak," are fine).
- **Directive:** Rewrite the incident summary load-free: "careless," "obviously," and "unfortunately" out; observable behavior in. The blameless-postmortem charter (§13) requires this pass.

### Weasel words (avoid)
- **Implied procedure:** Strike unattributed hedges that erase agency and verifiability — "some say," "it is believed," "arguably," "widely considered," "up to"; each claim acquires a named source or owner or leaves the document.
- **Replaces:** No "some might argue" — who? No "widely considered" — by whom, where? Every claim carries its owner or citation, and the ones that can't get deleted rather than hedged into deniability.
- **Ambiguity:** Adjacent to legitimate hedging (§11 hedge discipline: evidence-scaled uncertainty is fine; agency-erasing vagueness is not) — the discriminator is whether the hedge names a source or hides one.
- **Directive:** Weasel-pass the design doc: every "it is recommended" becomes "the SRE lead recommends" or dies; count before and after in the review notes.

### Euphemism treadmill (detect)
- **Implied procedure:** When a term is renamed, ask what practice the new term denotes; if the practice is unchanged, the rename is cosmetic; genuine reform changes practice and lets labels follow; watch for renamed-things quietly reacquiring the old stigma.
- **Replaces:** "Legacy modernization" that still ships through the same broken pipeline is a rename: describe what physically changes — if nothing does, we moved the word, not the problem, and the word will need replacing again next year.
- **Ambiguity:** Pinker's coinage about stigma cycles; not all renaming is euphemism (precision renames are legitimate — §17 operational definitions); the test is practice-tracing, which costs actual investigation.
- **Directive:** The "incident enablement" rename changes nothing until the on-call rotation and follow-up SLA change: trace the practice, then decide if the word earned itself.

### Presupposition audit
- **Implied procedure:** For each load-bearing sentence, list what must already be true for the sentence to be coherent; contested presuppositions surface and get argued before the sentence's question is answered; questions carry presuppositions hardest of all.
- **Replaces:** "Even the failed migration..." assumes the migration failed; "when did you stop..." assumes you started — before answering any question, drag out what it takes for granted and settle that first.
- **Ambiguity:** Linguistic presupposition vs. mere entailment is a technical boundary; in directive use, the deliverable is the assumptions list extracted from phrasing (smuggling detection); over-application turns every exchange into philosophy seminar — restrict to load-bearing sentences.
- **Directive:** Presupposition audit the incident question "why did the cache drop 40%?" — presupposes it dropped (verify), that it's one event (it's two), and that cache is the right variable (it's a symptom).

### Definitional collapse
- **Implied procedure:** Detect where one term silently serves two senses in a document; split into two named terms; assign one sense per term per document; re-verify every prior use against the split.
- **Replaces:** "Latency" means wire-RTT in section 2 and end-to-end in section 5: that document concludes nothing — split the word, name both senses, and re-check every use.
- **Ambiguity:** The failure is invisible in fluent prose (each local use reads fine — the collapse appears only at the joints); requires a second reader or a glossary pass to catch.
- **Directive:** "User" collapses across authenticated-account and seat-license in the pricing spec: split into "account" and "seat," re-verify every occurrence, and the compliance question answers itself.

### Unambiguous / unequivocal
- **Implied procedure:** Engineer the communication to admit exactly one reading: operationally defined terms, pinned scopes, expanded references; residual ambiguity is a defect with a fix, not a fact of prose; "clear enough" is not a category.
- **Replaces:** One reading, by construction: defined terms, pinned quantifier scope, expanded pronouns — and if two engineers could implement two systems from this text, the text is broken.
- **Ambiguity:** Meta-irony: as bare intensifiers both words are exactly the vague ornament this lexicon excludes — they steer only as flags demanding the mechanical checks (definitions, scope-pins, expansions).
- **Directive:** Make the API contract unambiguous the mechanical way: every term operationally defined, every quantifier scoped, every error path enumerated — then have two readers implement from text alone and diff their understanding.

### Deterministic
- **Implied procedure:** Same inputs produce same outputs and same execution path: randomness excluded or explicitly seeded, time and environment dependencies removed or injected; determinism is verified by double execution and full diff.
- **Replaces:** Identical in, identical out — including the path taken: no clock reads, no unseeded randomness, no ambient state; and you prove it by running it twice and diffing everything, including the logs.
- **Ambiguity:** Deterministic build (§7) vs. deterministic execution vs. deterministic response (an LLM output is not deterministic under default sampling — and even greedy paths drift across versions); "mostly deterministic" means no.
- **Directive:** The replay harness must be deterministic: fixed seeds, injected clock, hermetic inputs — two runs, diff including log order; any nondeterminism found gets a ticket, not a shrug.

### Canonical
- **Implied procedure:** Among equivalent representations, declare one the form; everything normalizes to it at the boundary; comparisons and storage happen only on canonical forms; parallel spellings of the same truth are treated as defects.
- **Replaces:** One officially chosen spelling of every thing: all equivalents get mapped onto it on the way in — two spellings of the same truth never coexist in the store where they can be counted as two things.
- **Ambiguity:** Canonical form (this sense) vs. canonical URL/ordering (specific instances) vs. canonical as "authoritative recommendation" (the literature sense); choosing a canonical form is a decision someone must own and document (§16 intent).
- **Directive:** Declare UTC ISO-8601 the canonical timestamp: normalize at every ingress; storage and comparison see only canonical form; non-canonical timestamps in output fail review.

## 18. Autonomous-Agent Operating Protocols
*Source fields: agent engineering, ops automation, this project's target use.*

### Bounded autonomy / permission envelope
- **Implied procedure:** Publish the tri-partition of actions — always allowed, never allowed, allowed on condition; execute freely within it; the envelope is versioned and auditable; expansion happens by change request, not by drift or discovery.
- **Replaces:** The written always/never/conditional list for this run: act without asking inside it, never cross it, and wanting more capacity is a request to amend the envelope — not something you discover mid-task.
- **Ambiguity:** The envelope must be enumerated, not gestured at ("be careful" is not an envelope); conditionals need checking machinery (§5 TOCTOU guard: conditions revalidated at use).
- **Directive:** Envelope v2 for this session: repo read-write, staging deploy, registry fetch; never: prod mutations, external sends, deletions. Conditional: anything costing >$1 — condition is explicit pre-approval.

### Stop-and-ask threshold
- **Implied procedure:** Predefine the ambiguity classes that force a question — irreversibility, missing authority, contradictory instructions, material consequence; below threshold, resolve autonomously and report; at threshold, stop and ask, arriving with options and a recommendation.
- **Replaces:** These situations mean ask first: one-way actions, out-of-authority actions, contradictory orders, and anything with real money or real blast; everything else you decide and log — and when you do ask, bring two options and a recommendation, not a pickle.
- **Ambiguity:** Threshold too low = helplessness theater (every step a question); too high = goal-hacking with confidence; the classes must be operational (the four above), not vibes like "important."
- **Directive:** Ask-classes for this task: destructive ops, third parties, spend, and any instruction contradicting the runbook. All else: proceed and log; when asking, attach Option A/B with your pick and why.

### Stuck detection
- **Implied procedure:** Detect non-progress signatures — same error twice, state unchanged after a claimed action, strategy cycling; on detection, halt the retry loop, switch strategy class (not instance), and report the blockage pattern with what was attempted.
- **Replaces:** Two identical failures in a row means you're stuck, not unlucky: stop repeating the same move, try a genuinely different kind of move, and if that fails too, stop and report exactly what you tried and what stood in the way.
- **Ambiguity:** Boundary between persistence and pathology is the retry pattern, not the count (legitimate long retries with varying approach pass); requires honest state-tracking to detect "unchanged."
- **Directive:** Stuck rule active: same exception twice → change approach (different library, different path, or read the actual source); second strategy fails → halt and report attempts, errors, and your read of the blocker.

### Thrash guard
- **Implied procedure:** Cap plan-revisions and approach-switches within a window; past the cap, freeze and escalate with state preserved; oscillation is detected as a pattern, not judged instance by instance.
- **Replaces:** Third replan on the same error is a pattern, not persistence: stop iterating, preserve what you know, and hand it up — endless polite retrying is how autonomous workers burn nights quietly.
- **Ambiguity:** Distinct from stuck detection (which catches repeated failure — this catches churning between alternatives); cap must be explicit (3 is a common default) and the escalation path must exist, or the guard just deadlocks.
- **Directive:** Thrash guard at 3: three approach switches on this bug without progress → freeze, write the summary of the three, page the human with artifacts attached.

### Replan triggers
- **Implied procedure:** Commit the plan; enumerate its invalidators — fact change, assumption failure, new constraint, threshold breach; on trigger, replan deliberately from the new state; silent mid-plan drift without a trigger is prohibited.
- **Replaces:** The plan is a commitment: here's what would legitimately invalidate it, and when one fires we re-plan on purpose from today's reality — otherwise we execute as written, not as mood suggests.
- **Ambiguity:** Adjacent to abort criteria (§4: end the operation) — triggers here cause re-planning, not necessarily stopping; under-specified triggers (anything "significant") collapse back to drift.
- **Directive:** Plan committed with triggers: any assumption marked false in the ledger, latency budget breach, or upstream schema change → replan session, new plan document, diff against old.

### Tool-output skepticism
- **Implied procedure:** Treat every tool and API response as a claim: check exit status and semantic success (the resource exists, content matches schema, magnitude plausible); assume parse errors and stale caches; verify before building; cite only what was actually returned.
- **Replaces:** A 200 OK is a claim, not a fact: GET the created thing back, check the payload against the schema, and never quote a line number you didn't see come back — tools fail politely and lie by omission.
- **Ambiguity:** Skepticism budget: verifying everything twice is paralysis — proportionate to consequence (§9); the no-fabrication constraint (§ below) is its memory-side twin.
- **Directive:** Post-create verification on all writes: after PUT, GET the resource and diff against intent; after search, sanity-check hit counts against magnitude expectations; anomalies in either → investigate before proceeding.

### Self-consistency (sampling)
- **Implied procedure:** For high-stakes derivations, run the reasoning multiple independent times with varied sampling; agreement across runs grades reliability; report convergent results with the disagreement rate attached; divergent outputs trigger method change, not averaging.
- **Replaces:** Run the extraction three separate times, independently, and keep only what all three runs agree on; the disagreement rate itself is the reliability number — averaging divergent answers is manufacturing a lie.
- **Ambiguity:** Costs multiply by sample count — reserve for load-bearing derivations; correlated failure modes (same prompt bias in every sample) defeat it; distinct from the Gricean maxim of the same name (consistency of assertion, §11).
- **Directive:** Self-consistency on the contract-term extraction: three samples, report only the intersection, and the divergence list goes to the human for adjudication.

### Reflexion loop
- **Implied procedure:** After a failed attempt, generate a structured self-critique against explicit criteria (what was missed, why, which constraint would have caught it); carry the lesson forward as a written constraint; iterate a bounded number of times; the critique is an artifact, not a mood.
- **Replaces:** When it fails, write down specifically which criterion you missed and add it as a rule for the next attempt — then try again with that rule, twice more at most, then escalate with the critiques attached.
- **Ambiguity:** Research-heritage term (Reflexion, Shinn et al.) drifting into buzzword; unbounded self-critique loops are the pathology (thrash guard interlock); the critique must change behavior, not just document regret.
- **Directive:** Reflexion discipline: each failed parse attempt appends one written constraint to the retry spec; after the third, stop and hand over the attempts plus the constraint list.

### Termination criteria
- **Implied procedure:** Define stop conditions before starting — done-state, budget exhausted, abort triggered, no-progress cap; execution ends exactly on the condition; each ending type has its report format; ending without finishing is a legitimate outcome.
- **Replaces:** Say in advance what ends this run: the goal state, the budget, the abort line, or the stuck-cap — and stop exactly there, reporting which one fired; running until you feel done is not a termination criterion.
- **Ambiguity:** Ends-without-goal must be culturally acceptable or the criteria get silently stretched; budgets include time, tokens, money, and side-effect count (§ tool budget below).
- **Directive:** Termination criteria pre-registered: done = suite green + docs updated; caps = 45 minutes, 200 tool calls, $5; abort = any envelope breach. Each fires its own report format; partial completion is reported as partial.

### Context hygiene / progressive summarization
- **Implied procedure:** Periodically compress working context: retain decisions, constraints, open questions, current state; discard process narrative; the compression is lossy by declared policy with the survivors named; the compressed form is the working record.
- **Replaces:** Every N steps, rewrite your notes down to the load-bearing facts — decisions made and why, constraints, open threads, where you are — the step-by-step story gets summarized away on purpose, or it eats the window.
- **Ambiguity:** Lossy by design: what must survive is a policy, not an instinct (decision provenance usually earns its tokens; debugging transcripts rarely do); compression timing is a tuning parameter, not a virtue.
- **Directive:** Context pass every 20 steps: rewrite the working file to decision/constraint/state/open-questions only; the full trace archives to the log, and the summary cites it by line.

### State externalization
- **Implied procedure:** Persist decision-state to durable storage after each meaningful step — done, decided, next; assume interruption at any point; resumption reads the ledger, not memory; the ledger is the primary, the context is a cache.
- **Replaces:** Write the state file after every step: what's done, what was decided and why, what's next — because you can be killed and replaced mid-task, and your successor resumes from the file, not from archaeology.
- **Ambiguity:** The ledger itself needs structure (append-only beats overwrite for audit — §7 WAL kinship); un-maintained ledgers are worse than none (they confidently lie); write-amplification cost on trivial tasks is real — scale to task size.
- **Directive:** PROGRESS.md is the primary state: append one entry per meaningful step (action, decision, reason, next); on any resume, start from it — never from a re-derivation of the repo.

### Handoff package
- **Implied procedure:** On ending a session, deliver the structured baton: current state, decisions with reasons, blockers, and the next concrete action including its exact command; written for a competent stranger who has your artifacts but not your memory.
- **Replaces:** End every session by passing the baton: where things stand, what was decided and why, what's stuck, and the literal next command to run — a stranger picks this up cold and moves without a meeting.
- **Ambiguity:** Distinct from SITREP (§10: periodic status) — this is terminal and complete; "next command" concreteness is the quality bar (a next-step that needs interpretation will be misinterpreted).
- **Directive:** Session ends with HANDOFF.md: state summary, decision log (one line each), blockers with attempted fixes, and the next command copy-pasteable — assume the reader is you-with-amnesia.

### No-fabrication constraint
- **Implied procedure:** Generate nothing ungrounded: no sources, quotes, values, paths, or line numbers not produced by an actual read or retrieval; unknowns are stated as unknowns; the observed/invented distinction is maintained under pressure to be helpful.
- **Replaces:** If you didn't read it, don't cite it: no invented file paths, no plausible-looking line numbers, no references that feel right — "I don't have that" is a complete, correct, and preferred answer.
- **Ambiguity:** Fluency impersonates grounding — confident prose is not evidence; the constraint collides with helpfulness norms exactly when the unknown is disappointing; sampling-level fabrication (a real file, wrong contents) needs verification, not just citation.
- **Directive:** No-fabrication standing rule: every path, number, and quote in your report traces to a tool result shown in the transcript; anything you can't trace gets labeled "unverified" or omitted.

### Uncertainty verbalization
- **Implied procedure:** In every report, separate confident claims from known-unknowns; for each unknown, state what would resolve it; fluent prose must never imply more certainty than the evidence supports; the map of unknowns is part of the deliverable.
- **Replaces:** Label what you know versus what you don't, every time, and for each unknown say what would settle it — smooth writing is not evidence, and it must not be allowed to impersonate it.
- **Ambiguity:** Pairs with estimative language (§1: the scale) and hedge discipline (§11: the surface form) — this is the structural requirement behind both; over-listing trivia-unknowns dilutes the signal (materiality filter).
- **Directive:** Every finding report ends with a Known-Unknowns block: each item states the question, why it matters, and the measurement that would close it — three items max, ranked.

### Bounded tool budget
- **Implied procedure:** Cap calls, tokens, time, and spend per task; track burn against the cap continuously; at 80% utilization, report and elect — finish narrower, or request more; budget exhaustion is a termination criterion, not a surprise.
- **Replaces:** The envelope is 200 calls, one hour, five dollars: watch your own burn rate, say something at 80%, and never discover the limit by slamming into it at full speed.
- **Ambiguity:** Budgets need instrumentation (self-report drifts); retry storms are the classic budget-eater (backoff + poison classification interlock); too-tight budgets cause premature narrowing — set them from task class, not vibes.
- **Directive:** Budget posted: 200 calls / 60 min / $5. At the 80% mark you post a burn report and your completion plan; hitting 100% without a posted plan is the defect, not the exhaustion itself.

### Retriable vs. poison classification
- **Implied procedure:** Classify each failure on arrival: retriable (transient — 429, timeout, 5xx) enters backoff-with-jitter; poison (deterministic — 400, 422, schema mismatch) quarantines immediately with its payload and diagnostics; misclassifications in both directions are tracked.
- **Replaces:** Not every failure deserves a retry: transient errors back off and retry; deterministic errors go straight to quarantine with their payload attached — retrying a malformed request a hundred times is how queues and budgets die.
- **Ambiguity:** Borderline classes (409 races, partial success) need explicit policy; quarantine without a review SLA is a landfill; the classification itself can be wrong (a "deterministic" 422 from a caching layer is transient) — track and revise.
- **Directive:** Every failure gets tagged RETRY or POISON at catch time: retries go through the backoff wrapper; poisons land in the dead-letter with full context; the weekly report reviews the DLQ and any tag reversals.

### Exception-only escalation
- **Implied procedure:** Resolve deviations independently within your authority; escalate only when intervention is genuinely required — one-way action, beyond-envelope, material risk; the escalation carries your resolution attempt and what you need, not just the problem.
- **Replaces:** Handle what you can, escalate what you must: when you do raise something, it arrives with what you tried, what you found, and precisely what you need from the human — a clean handoff of an attempt, not a relay of a problem.
- **Ambiguity:** Distinct from exception-only reporting (§10: what appears in routine output — this governs when to pull a human into action); under-escalation (heroic silent grinding) is the characteristic failure, and it's invisible until the budget report.
- **Directive:** Escalation bar: pull a human only for one-way, out-of-envelope, or material-risk deviations; every escalation includes attempt log, current state, and the specific ask; everything else resolves and appears in the exception report.

### Autonomy cluster (autonomous / self-sufficient / proactive / resourceful)
- **Implied procedure:** Four independence adjectives, four distinct duties: autonomous — act within authority without per-step instruction; self-sufficient — exhaust available means before requesting help; proactive — surface risks and next steps unasked; resourceful — substitute means when the preferred one fails.
- **Replaces:** Four standing duties, not four compliments: decide inside your envelope, exhaust your own tools first, bring us problems while they're small, and when the front door is locked, find the side door — each is an assignment with a test, not praise.
- **Ambiguity:** As praise they decorate; as assignments they steer — all four are bounded by the envelope (§ above) and the stop-and-ask threshold; "proactive" without an envelope is scope creep with confidence; "resourceful" without the no-fabrication constraint is where hallucinated shortcuts breed.
- **Directive:** This engagement's standing duties: autonomous within the posted envelope, self-sufficient through the listed tools, proactive on risk (surface at suspicion, not at damage), resourceful by substitution — never by invention (no-fabrication stands).

---

## Steering Map

Choose tokens by the behavior you need to induce; compound across columns for full stances.

| Behavioral objective | Highest-leverage terms |
|---|---|
| Make it verify before believing | corroborate, triangulate, ground truth, reproduce, cross-reference, negative control, tool-output skepticism |
| Make it skeptical of its own reasoning | falsify, ACH, premortem, consider the opposite, self-consistency, differential diagnosis |
| Make it cautious and contained | ask-before-act, blast radius, least privilege, fail closed, primum non nocere, surgical, scope containment |
| Make it precise in language | operational definition, quantifier-scope pinning, unambiguous (mechanical), canonical, verbatim quoting discipline |
| Make it recover from failure | abort criteria, backout plan, rollback, compensating action, snapshot-before-mutate, idempotent, circuit breaker |
| Make it report usefully | BLUF, pyramid principle, MECE, SITREP, exception-only reporting, evidential markers, decision-ready communication |
| Make it persistent under failure | backoff with jitter, retriable-vs-poison, stuck detection, thrash guard, state externalization, handoff package |
| Make it delegate safely / be delegated to | commander's intent, mission-type orders, ROE, bounded autonomy, two-way doors, initiative in absence |
| Make it finish | definition of done, exit criteria, termination criteria, YAGNI, scope containment, timebox |
| Make it learn and prevent recurrence | blameless postmortem, causal stack, Swiss cheese, institutionalized lessons, error budget, normalization-of-deviance guard |
| Make it resist manipulation | salami tactics, nibble, loaded language, presupposition audit, probing action, weasel words |
| Make it honest about uncertainty | estimative language, calibration training, uncertainty verbalization, null-result discipline, hedge discipline |

## Maintenance & Expansion Protocol

1. **Mint rule.** When an expanded instruction recurs three or more times across directives, promote it: write the entry (five fields), assign its domain, and use the address thereafter.
2. **Retirement test.** Any term whose expansion test (§3.1) fails across target models — the expansion is wrong, contested, or empty — gets demoted to the expanded instruction, or annotated with the gloss it needs.
3. **Ranking properties** (per `docs/PURPOSE.md`): score candidates on procedural richness, specificity, stability, model familiarity, and token cost. This lexicon supplies the human-expert side — implied-procedure fields are hand-derived procedural richness; the density flags (ascertain, scrutinize, elucidate, safeguard, anticipate, streamline, comprehensive) mark known weakness. The database pipeline (FrameNet for frames evoked, VerbNet for implied action structure, WordNet + information content for specificity, psychNorms for familiarity/ambiguity, O*NET for professional procedure discovery) extends candidate discovery beyond hand curation.
4. **Empirical validation.** Steering power is only established by testing: equivalent instructions against identical tasks across models, comparing adherence, consistency, side effects, and token cost — store results in SQLite keyed to the term (POSIX-style sensitivity testing; APE/DSPy-style optimization for wording variants).
5. **End state.** The reverse dictionary for agent behavior: describe the desired behavior, retrieve the shortest reliably-effective instruction that induces it. This lexicon's TSV (`semantic_lexicon.tsv`) is the seed corpus for that index; every entry's `replaces_instruction` column is the behavior-description side of the lookup.
