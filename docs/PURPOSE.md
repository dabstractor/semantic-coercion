# **High-density vocabulary for LLM prompts**

## **Objective**

Build a searchable vocabulary of English words and established phrases that elicit complex, precise, and reliable agent behavior with minimal tokens.

For example, **"Conduct a structured interrogation"** invokes an established process without explicitly describing each step.

The goal is **behavioral effectiveness per token**, not sophisticated vocabulary for its own sake.

## **Free downloadable databases**

All of these can be processed locally without paid APIs.

| Database       | Useful information                                                                                                | Download                                                                                                                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FrameNet**   | Words that evoke entire situations, processes, and relationships. Best starting point.                            | [ZIP](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/framenet_v17.zip?utm_source=chatgpt.com) · [Python API](https://www.nltk.org/howto/framenet.html?utm_source=chatgpt.com) |
| **VerbNet**    | Verbs grouped by the actions and logical relationships they imply.                                                | [ZIP](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/verbnet3.zip?utm_source=chatgpt.com) · [GitHub](https://github.com/cu-clear/verbnet/?utm_source=chatgpt.com)             |
| **WordNet**    | Related concepts, specificity, implied meanings, and synonyms.                                                    | [ZIP](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip?utm_source=chatgpt.com) · [Python API](https://www.nltk.org/howto/wordnet.html?utm_source=chatgpt.com)       |
| **WordNet IC** | Numerical estimates of conceptual specificity based on usage frequency.                                           | [ZIP](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet_ic.zip?utm_source=chatgpt.com)                                                                                   |
| **psychNorms** | 291 word-level measurements, including familiarity, frequency, ambiguity, and number of associated attributes.    | [GitHub](https://github.com/zak-hussain/psychnorms?utm_source=chatgpt.com)                                                                                                                                |
| **O\*NET**     | 19,000+ professional tasks and 2,000+ work activities. Useful for discovering established procedural terminology. | [Database downloads](https://www.onetcenter.org/database.html?utm_source=chatgpt.com)                                                                                                                     |
| **SemLink**    | Cross-references between FrameNet, VerbNet, and PropBank. Useful when combining databases.                        | [GitHub](https://github.com/cu-clear/semlink?utm_source=chatgpt.com)                                                                                                                                      |

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+6

None directly measures LLM steering power. They provide data from which useful candidates can be discovered and ranked.

## **Installation**

```
uv add nltk
uv run python -m nltk.downloader \
  framenet_v17 verbnet3 wordnet wordnet_ic

git clone https://github.com/zak-hussain/psychnorms.git
```

## **Querying the databases**

**FrameNet:** Retrieve the larger concepts associated with a word, their components, and related vocabulary.

```
from nltk.corpus import framenet as fnfor frame in fn.frames_by_lemma(r"scrutinize\.v"):    print(frame.name)    print(frame.definition)    print(list(frame.FE.keys()))    print(list(frame.lexUnit.keys()))
```

**VerbNet:** Retrieve related verbs and the actions they imply.

```
from nltk.corpus import verbnet3 as vnfor cls in vn.classids(lemma="inspect"):    print(cls)    print(vn.lemmas(cls))    print(vn.frames(cls))
```

**WordNet:** Retrieve definitions, related concepts, implied actions, and numerical specificity scores.

```
from nltk.corpus import wordnet as wn, wordnet_icfrom nltk.corpus.reader.wordnet import information_contentic = wordnet_ic.ic("ic-brown.dat")for sense in wn.synsets("audit", pos=wn.VERB):    print(sense.definition())    print(sense.lemma_names())    print(sense.entailments())    print(sense.hypernyms())    print(information_content(sense, ic))
```

**psychNorms:** Inspect the available measurements and their descriptions before selecting useful columns.

```
import csvwith open("psychNorms/psychNorms_metadata.csv") as f:    for row in csv.DictReader(f):        print(row["norm"], row["description"])
```

## **Candidate discovery**

Useful terminology frequently comes from established professional practices rather than ordinary synonyms.

| Category      | Examples                                               |
| ------------- | ------------------------------------------------------ |
| Investigation | Scrutinize, corroborate, triangulate, ascertain, audit |
| Reasoning     | Reconcile, synthesize, falsify, deduce, extrapolate    |
| Communication | Disambiguate, contextualize, distill, elucidate        |
| Execution     | Orchestrate, operationalize, consolidate               |
| Restraint     | Parsimonious, judicious, surgical, proportional        |
| Verification  | Substantiate, attest, reproduce, validate              |
| Prevention    | Preempt, anticipate, mitigate, safeguard               |

Established phrases can carry considerably more procedural meaning:

| Phrase                       | Implied behavior                                       |
| ---------------------------- | ------------------------------------------------------ |
| Structured interrogation     | Systematically elicit missing information              |
| Due diligence                | Investigate and verify before committing               |
| Adversarial review           | Actively seek weaknesses and counterexamples           |
| Root cause analysis          | Investigate causes rather than symptoms                |
| Progressive disclosure       | Reveal information only as needed                      |
| Exception-only escalation    | Resolve independently unless intervention is necessary |
| Exhaustive enumeration       | Account for every member of a defined set              |
| Differential diagnosis       | Systematically distinguish competing explanations      |
| Steelman                     | Construct the strongest opposing argument              |
| First-principles reasoning   | Derive conclusions from fundamental facts              |
| Least astonishment           | Favor predictable behavior                             |
| Scope containment            | Prevent unnecessary expansion of work                  |
| Decision-ready communication | Present recommendations and material consequences      |

## **Vocabulary-mining prompt**

Compile an extensive lexicon of semantically dense English words and established phrases that evoke methodologies, procedures, reasoning patterns, or behavioral constraints.

Prioritize behavioral specificity, implicit meaning, and steering power per token. Exclude ornamental vocabulary, vague intensifiers, and redundant synonyms.

Mine established terminology across professional and scientific disciplines.

For each entry, record the term, implied behaviors, expanded instruction it replaces, ambiguities, and example agent directive.

## **Ranking candidates**

Measure five properties:

| Property            | Desired quality                     |
| ------------------- | ----------------------------------- |
| Procedural richness | Implies numerous relevant behaviors |
| Specificity         | Constrains behavior precisely       |
| Stability           | Consistently interpreted            |
| Model familiarity   | Reliably understood by the model    |
| Token cost          | Inexpensive to express              |

Database measurements can help shortlist candidates. Actual effectiveness must be established through model testing.

Run equivalent instructions against identical tasks across multiple models. Compare adherence, consistency, unintended behavior, and token consumption. Store results in SQLite alongside the source vocabulary.

## **Relevant research and tools**

| Resource                                                                                                  | Application                                                    |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [Frame semantics](https://www.nltk.org/howto/framenet.html?utm_source=chatgpt.com)                        | Discover words that invoke larger conceptual structures        |
| [POSIX](https://aclanthology.org/2024.findings-emnlp.852/?utm_source=chatgpt.com)                         | Research measuring model sensitivity to prompt wording         |
| [Automatic Prompt Engineer](https://mlanthology.org/iclr/2023/zhou2023iclr-large/?utm_source=chatgpt.com) | Automatically generate and evaluate instructions               |
| [DSPy GEPA](https://dspy.ai/current/tutorials/gepa_ai_program/?utm_source=chatgpt.com)                    | Iteratively optimize instructions against measured performance |
| [Datamuse API](https://www.datamuse.com/api/?utm_source=chatgpt.com)                                      | Discover vocabulary from descriptions of desired meaning       |

## **Recommended implementation**

Download FrameNet, VerbNet, WordNet IC, and psychNorms. Normalize their useful contents into SQLite. Give an agent searchable access to the data and the vocabulary-mining prompt above. Use O\*NET to supplement discovery of established professional procedures.

Ultimately, build a **reverse dictionary for agent behavior**: describe the desired behavior and retrieve the shortest, most reliably effective instructions for inducing it.
