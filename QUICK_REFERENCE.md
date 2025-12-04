# Neuro-Omics-KB Quick Reference

> **🔗 Quick Links:** [📖 Docs Site](https://allison-eunse.github.io/neuro-omics-kb/) | [🧬 Genetics Models](https://allison-eunse.github.io/neuro-omics-kb/models/genetics/) | [🧠 Brain Models](https://allison-eunse.github.io/neuro-omics-kb/models/brain/) | [🔗 Integration](https://allison-eunse.github.io/neuro-omics-kb/integration/)

---

## 📍 Repository Structure

### Neuro-Omics KB (This Repository)
**GitHub**: https://github.com/allison-eunse/neuro-omics-kb  
**Docs**: https://allison-eunse.github.io/neuro-omics-kb/  
**Purpose**: Knowledge base - documentation, YAML cards, walkthroughs

---

## 🎯 Repository Overview

### Documentation
```
docs/code_walkthroughs/
├── Brain FMs (5):
│   ├── brainharmony_walkthrough.md  (Hub-token fusion)
│   ├── brainjepa_walkthrough.md     (JEPA latent forecast)
│   ├── brainlm_walkthrough.md       (BrainLM MAE guide)
│   ├── brainmt_walkthrough.md       (BrainMT Mamba+Transformer)
│   └── swift_walkthrough.md         (Swin 4D fMRI)
├── Genetics FMs (4):
│   ├── caduceus_walkthrough.md      (RC-equivariant Hyena)
│   ├── dnabert2_walkthrough.md      (BPE tokenization)
│   ├── evo2_walkthrough.md          (StripedHyena 1M context)
│   └── generator_walkthrough.md     (6-mer generative model)
└── Multimodal/Clinical (6):
    ├── bagel_walkthrough.md         (Unified multimodal)
    ├── mot_walkthrough.md           (Mixture-of-Transformers)
    ├── m3fm_walkthrough.md          (Multilingual CXR)
    ├── melamma_walkthrough.md       (Medical LLM)
    ├── titan_walkthrough.md         (Whole-slide imaging)
    └── fms_medical_walkthrough.md   (FM catalog)
```

### Metadata Cards
```
kb/
├── model_cards/       (9 models: all valid YAML)
├── datasets/          (13 datasets + UKB manifest)
├── integration_cards/ (Embeddings + harmonization strategies)
└── paper_cards/       (14 structured research papers)
```

### Management
```
scripts/
├── manage_kb.py        (validation tool)
├── codex_gate.py       (quality gate)
└── fetch_external_repos.sh
```

---

## 🚀 Common Commands

### Neuro-Omics-KB

```bash
# Serve documentation
mkdocs serve

# Validate model cards
python scripts/manage_kb.py validate models

# Validate dataset cards
python scripts/manage_kb.py validate datasets

# Query embedding strategies
python scripts/manage_kb.py ops strategy smri_free_surfer_pca512_v1

# Query harmonization methods
python scripts/manage_kb.py ops harmonization murd_t1_t2

# Check YAML syntax
python -c "import yaml; from pathlib import Path; \
[print(f'✓ {f.stem}') for f in Path('kb/model_cards').glob('*.yaml') \
if f.stem != 'template' and yaml.safe_load(f.read_text())]"

# Codex gate (fast / full)
python scripts/codex_gate.py --mode fast --label cycle1 --since origin/main
python scripts/codex_gate.py --mode full --label cycle2 --since HEAD~1
```

---

## 📊 Repository Stats

### Neuro-Omics-KB (Updated Dec 4, 2025)
- **Code Walkthroughs**: 15+ complete guides (brain + genetics + multimodal)
- **Model Cards**: 18+ YAML files (core FMs + reference architectures + ARPA-H planning cards)
- **Paper Cards**: 31+ structured cards
- **Dataset Cards**: 20+ specifications (includes planning cards for pending UKB data)
- **Integration Guidance**: 7+ YAML registries + 3 narrative integration cards
- **Experiment Configs**: 10 YAMLs (3 production templates + 7 dev/ablation stubs)
- **External Repos**: 15+ reference implementations (mix of tracked snapshots + fetch-on-demand)

---

## 🤖 Using Parallel Agents in Cursor

- **What parallel agents do**: Cursor runs multiple isolated agents in parallel from **one prompt**, each restricted to different parts of the repo according to `.cursor/agent-manifest.json`.

- **Your agents**:
  - **Brain agent**: brain models, brain walkthroughs, brain datasets, brain paper/model cards, `external_repos/brain*`, `swift`.
  - **Genetics agent**: genetics models, genetics walkthroughs, DNA/benchmark datasets, genetics paper/model cards, `external_repos/caduceus|dnabert2|evo2|generator`.
  - **Integration agent**: `docs/integration/`, `docs/data/`, all model docs/walkthroughs, all KB cards (integration + cross-domain).
  - **RAG/scripts agent**: `scripts/`, `rag/`, `kb/rag/`.
  - **Master/coherence agent**: reads the whole project but should only **edit** meta files (README, summaries, KB READMEs, key integration cards).

### How to write prompts for parallel agents

- **Cross-domain update example** (brain + genetics + integration):

  > "You are part of a team of domain agents (brain, genetics, integration, scripts, master).  
  > In **your own domain slice**, update any relevant docs and KB cards so that the description and usage of the UKB fMRI and genetics datasets are consistent across model cards, dataset cards, and walkthroughs.  
  > Do not edit files that are clearly outside your domain. At the end, summarize exactly which files you changed and why."

- **Master coherence pass example**:

  > "Act as the **Global master / coherence agent**.  
  > Read across the project to check naming and conceptual consistency between brain and genetics sections.  
  > You may only edit: README, ORGANIZATION_SUMMARY, QUICK_REFERENCE, TREE_VIEW, docs index/integration docs, KB section READMEs, and the integration cards for genetics embeddings and UKB alignment.  
  > Propose and apply small edits to those meta files so they accurately describe the current structure and relationships in the KB."

---

## ✅ What's Clean

- ✅ Implementation repos live under `external_repos/` (bagel, MoT snapshots) with the remainder fetched on demand
- ✅ All YAML cards parse successfully
- ✅ All walkthroughs complete with KB reference links
- ✅ README clarified (KB-only purpose)
- ✅ PDF tools moved to separate repo
- ✅ Coherent structure across all model documentation

---

## 📝 Next Steps

### For Neuro-Omics-KB:
1. Continue documenting models and integration strategies
2. Keep YAML cards updated with new checkpoints
3. Expand integration playbooks in `docs/integration/`
4. Fill in dataset manifests after data inventory meetings

### For Contributors:
1. Review `README.md` + KB overview for scope and contact the maintainer (README bottom) before large edits
2. Use templates in `kb/*/template.yaml` for new cards
3. Validate changes with `python scripts/manage_kb.py`

---

## 🔗 Quick Navigation

### Documentation
- **Main KB Index**: [docs/index.md](https://allison-eunse.github.io/neuro-omics-kb/)
- **Code Walkthroughs**: [docs/code_walkthroughs/](https://allison-eunse.github.io/neuro-omics-kb/code_walkthroughs/)
- **Integration Strategy**: [docs/integration/integration_strategy.md](https://allison-eunse.github.io/neuro-omics-kb/integration/integration_strategy/)
- **Analysis Recipes**: [docs/integration/analysis_recipes/](https://allison-eunse.github.io/neuro-omics-kb/integration/analysis_recipes/)
- **Integration Plan**: [docs/decisions/2025-11-integration-plan.md](https://allison-eunse.github.io/neuro-omics-kb/decisions/2025-11-integration-plan/)

### Cards
- **Model Cards**: `kb/model_cards/`
- **Paper Cards**: `kb/paper_cards/`
- **Dataset Cards**: `kb/datasets/`
- **Integration Cards**: `kb/integration_cards/`

### Configs & Tools
- **Experiment Configs**: `configs/experiments/`
- **KB Script**: `scripts/manage_kb.py`

---

**Last Updated**: December 4, 2025  
**Organized by**: Allison Eun Se You  
**Status**: ✅ Documentation Framework Complete — Awaiting Data Availability

**Data Status:**
- 🟡 **UKB Covariates**: Planning card created; data extraction pending UKB project approval
- 🟡 **Genetics Embeddings**: Planning card created; embeddings NOT YET computed (pending UKB WES access)
- 🟡 **UKB fMRI/sMRI**: Pipeline documented; data extraction pending
- 🟢 **Reference Datasets**: hg38, genomic benchmarks available

**KB Purpose Reminder:** This is a **documentation-first knowledge base**—not running code. Implementation code lives in upstream `external_repos/`. Cards marked "planning" or "reference_model" are for documentation/architectural reference only.
