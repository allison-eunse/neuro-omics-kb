Neurogenomics KB

## Purpose

A **documentation-focused knowledge base** for genetics and brain foundation models and their multimodal integration, now extended to **gene–brain–behaviour foundation models** across both **adult** and **developmental / neurodevelopmental** cohorts. This repository contains structured documentation, YAML metadata cards, code walkthroughs, and integration strategies that span **genetic FMs**, **brain FMs** (MRI/fMRI), **EPhys/EEG FMs**, and downstream behavioural/clinical phenotypes.

This KB **originated** as an **adult UK Biobank–centric gene–brain FM alignment** effort (genetics FM + MRI-derived phenotypes) and has since been broadened to cover **longitudinal, multimodal gene–brain–behaviour FMs**, including MRI, EEG, genetics, and developmental / behavioural trajectories over time.

Within an ARPA-H–style ecosystem, neurogenomics-kb treats:
- **Brain FM** as MRI/fMRI foundation models,
- **EPhys/EEG FM** as electrophysiology/EEG foundation models,
- **Multi-Omics FM** as genomics + other omics FMs, and
- a large-scale **Brain-Omics Model (BOM)** as the integrated brain–omics–LLM FM where an **LLM acts as a semantic bridge / common hub** tying together brain signals, omics, behaviour, and language.

**Note:** This is a **knowledge base only** - no implementation code. For actual model training/inference, refer to the `external_repos/` directories or the original model repositories (run `./scripts/fetch_external_repos.sh` to clone them locally).

## What's Inside

### 📚 Documentation (`docs/`)
- **Code Walkthroughs**: In-depth guides for 9 foundation models
  - Genomics (4): Caduceus, DNABERT-2, GENERator, Evo 2
  - Brain (5): BrainLM, Brain-JEPA, Brain Harmony, BrainMT, SwiFT
- **Integration Playbooks**: Strategies for multimodal fusion, from late fusion baselines to ARPA-H–style Brain-Omics Model (BOM) integration.
- **Data Schemas**: UK Biobank, HCP, and other datasets, with an expanding scope toward **developmental / neurodevelopmental** cohorts and longitudinal designs.
- **Decision Logs**: Architectural and research choices, including when to escalate from standalone neurogenomics analyses to larger brain–omics–LLM FMs.
- **Curated Paper Sources**: Every PDF pulled via `pdf<->md;ai-summaries` is stored under `docs/generated/kb_curated/papers-pdf/` with its Markdown counterpart in `docs/generated/kb_curated/papers-md/`. Keep both in sync—they are the citation backbone for the YAML paper/model cards.

### 🏷️ Metadata (`kb/`)
- **Model Cards** (`model_cards/*.yaml`): Structured metadata for each FM (genetic FMs, brain FMs, and future EEG / multi-omics FMs).
- **Dataset Cards** (`datasets/*.yaml`): Specs with counts, subset breakdowns, access/licensing notes, modality-specific column maps, longitudinal structure, and base-pair stats; each links to `external_repos/` + relevant walkthroughs for reproducible extraction.
- **Integration Cards** (`integration_cards/*.yaml`): Multimodal fusion strategies and pipelines, including **gene–brain**, **gene–brain–behaviour**, and future **gene–brain–EEG** recipes.
- **Embedding Strategy Registry** (`integration_cards/embedding_strategies.yaml`): Canonical per-modality recipes (segment/run hierarchy, preprocessing, projector, `sources`) for genetics, MRI/fMRI, and—going forward—EEG/EPhys and behavioural latents.
- **Harmonization Catalog** (`integration_cards/harmonization_methods.yaml`): `none` vs. ComBat vs. MURD vs. unlearning, with references and intended project usage.
- **rs-fMRI Preprocessing Pipelines** (`integration_cards/rsfmri_preprocessing_pipelines.yaml`): Named stacks such as `hcp_like_minimal` that experiments can cite.
- **Paper Cards** (`paper_cards/*.yaml`): Research paper references and integration principles.

In addition to these, neurogenomics-kb is growing a set of **standard schemas** for:
- **EEG / EPhys features** (segment definitions, channel layouts, frequency bands, task paradigms),
- **developmental and behavioural scores** (e.g., ASD/ADHD scales, cognitive tests, developmental milestones),
- **clinical labels and longitudinal visit structure** (diagnostic trajectories, comorbidities, visit windows, and wave IDs).

It also aims to store **semantic alignment recipes** (as integration / embedding strategy cards) for:
- aligning **gene / brain / EEG embeddings to language** via LLMs as a semantic hub, and
- aligning **images or video to text** via vision–language models (VLMs),
so that future LLM/VLM alignment work has clear, documented precedents.

### 🔗 External Repos (`external_repos/`)
- Git-ignored working copies synced via `./scripts/fetch_external_repos.sh`
- Table of upstream links documented in `external_repos/README.md`

### 🔧 KB Management (`scripts/`)
- `manage_kb.py`: Validation and catalog generation tools
- No implementation scripts (moved to separate repos)

## Build & Serve Locally

```bash
# Install dependencies
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# (Optional) fetch upstream model repos for reference
./scripts/fetch_external_repos.sh

# Serve documentation site
mkdocs serve

# Validate YAML cards
python scripts/manage_kb.py validate models
python scripts/manage_kb.py validate datasets
```

### Trace embedding/harmonization IDs

Every experiment config references embedding and harmonization IDs. Use the helper commands to print the latest recipe before running extraction:

```bash
# Show the full sMRI baseline recipe
python scripts/manage_kb.py ops strategy smri_free_surfer_pca512_v1

# Inspect harmonization metadata (e.g., MURD)
python scripts/manage_kb.py ops harmonization murd_t1_t2
```

Log these IDs (and the preprocessing pipeline, e.g., `rsfmri_preprocessing_pipelines.hcp_like_minimal`) with any downstream run so results remain reproducible.

### Generated assets stay in-repo

- `docs/generated/kb_curated/` contains the Markdown + PDF artifacts produced by the companion `pdf-md-ai-summaries` project; reference these instead of embedding snippets directly into YAML.
- `docs/generated/templates/` keeps scaffold files for future cards/recipes—copy, do not edit in place.

## Codex Quality Gate (2-Cycle Workflow)

Use `scripts/codex_gate.py` to enforce an automatic pass/fail gate whenever you run Codex in two consecutive cycles. The gate bundles domain tests (`manage_kb` validators + MkDocs), Python linting (`ruff`), and static type checks (`mypy`), then records the outcome so Cycle 2 can compare itself to Cycle 1.

```
# Cycle 1 – quick sanity before giving Codex control
python scripts/codex_gate.py --mode fast --label cycle1 --since origin/main

# Cycle 2 – full sweep before handing work back
python scripts/codex_gate.py --mode full --label cycle2 --since HEAD~1
```

- `--mode fast` skips the MkDocs build for a faster signal; `--mode full` runs everything.
- `--since` scopes checks to paths that changed versus the provided git ref (fallback: run all).
- Results are stored under `~/.cache/codex_gate/neurogenomics-kb` (override via `--state-dir`).
- `--fail-fast` stops on the first failure, and `--list-checks` shows the exact commands.

If Cycle 2 introduces a regression, the gate exits with a non-zero status so the automation can halt before launching the next Codex pass.

## Usage

### Explore Model Cards
```bash
# List all models
ls kb/model_cards/*.yaml

# View a specific model
cat kb/model_cards/caduceus.yaml
```

### Read Code Walkthroughs
```bash
# Open in browser after serving
mkdocs serve
# Visit: http://localhost:8000/code_walkthroughs/caduceus_walkthrough/
```

### Reference External Code
```bash
# External repos are for reference only
cd external_repos/caduceus
# Follow original repo instructions for training/inference
```

## Contribution Guidelines

This is a **documentation repository**. Contributions should focus on:

✅ **Do:**
- Add/update model cards with accurate metadata
- Write comprehensive code walkthroughs
- Document integration strategies
- Add decision logs for architectural choices
- Improve data schemas and benchmarks

❌ **Don't:**
- Add implementation code (training scripts, inference pipelines)
- Include custom model variants
- Create helper scripts for embeddings extraction
- Add experimental code

### YAML Card Guidelines
- Keep `verified: false` until human review
- Include all required fields (see `kb/*/template.yaml`)
- Reference external repos for implementation details
- Use links for code examples, not inline code

### Documentation Style
- Concise with citations
- Link to original papers and repos
- Include practical integration examples
- Focus on "how to use" not "how to implement"

## Role in larger Brain–Omics–LLM FM efforts

In addition to standalone neurogenomics analyses, **neurogenomics-kb** serves as the **neurogenomics documentation layer / sub-KB** inside larger multimodal brain–omics–LLM FM efforts (e.g., ARPA-H–style **Brain-Omics Model (BOM)**). It documents models, datasets, and integration recipes so that **gene–brain–behaviour FMs**—spanning adult and developmental cohorts, MRI/fMRI, EEG/EPhys, genetics, behavioural/developmental assessments, and language—can be scaled, compared, and reproduced across cohorts and projects.

## Related Repositories

- **PDF/Markdown Converter**: [pdf-md-ai-summaries](https://github.com/allison-eunse/pdf-md-ai-summaries)
- **Model Implementations**: See links in individual model cards
- **Datasets**: UK Biobank (restricted), HCP, OpenGenome2

## Contact

**Maintainer**: Allison Eun Se You  
**Purpose**: Knowledge base for neurogenomics foundation model research  
**Scope**: Documentation, metadata, integration strategies (no implementation)
