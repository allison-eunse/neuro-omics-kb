# Neurogenomics-KB Quick Reference

## 📍 Repository Locations

### 1. **Neurogenomics KB** (Documentation & Metadata)
**Location**: `/Users/allison/.cursor/worktrees/neurogenomics-kb/2wmpo/`  
**GitHub**: (your existing repo)  
**Purpose**: Knowledge base - documentation, YAML cards, walkthroughs

### 2. **PDF Converter** (Separate Utility)
**Location**: `/Users/allison/Projects/pdf<->md;ai-summaries/`  
**GitHub**: https://github.com/allison-eunse/pdf-md-ai-summaries  
**Purpose**: PDF↔MD conversion + AI summaries

---

## 🎯 Neurogenomics-KB Structure

### Documentation
```
docs/code_walkthroughs/
├── brainharmony_walkthrough.md  (Hub-token fusion)
├── brainjepa_walkthrough.md     (JEPA latent forecast)
├── brainlm_walkthrough.md       (BrainLM MAE guide)
├── brainmt_walkthrough.md       (BrainMT Mamba+Transformer)
├── caduceus_walkthrough.md      (RC-equivariant Hyena)
├── dnabert2_walkthrough.md      (BPE tokenization)
├── evo2_walkthrough.md          (StripedHyena 1M context)
├── generator_walkthrough.md     (6-mer generative model)
├── swift_walkthrough.md         (Swin 4D fMRI)
└── index.md
```

### Metadata Cards
```
kb/
├── model_cards/       (7 models: all valid YAML)
├── datasets/          (11 datasets + UKB manifest: HF counts, subset splits, access/licensing, modality columns, base-pair stats)
├── integration_cards/ (2 cards: embeddings + alignment)
└── paper_cards/       (templates ready)
```

### Management
```
scripts/manage_kb.py    (validation tool)
```

---

## 🚀 Common Commands

### Neurogenomics-KB

```bash
# Navigate to KB
cd /Users/allison/.cursor/worktrees/neurogenomics-kb/2wmpo

# Serve documentation
mkdocs serve

# Validate model cards
python scripts/manage_kb.py validate models

# Validate dataset cards
python scripts/manage_kb.py validate datasets

# Check YAML syntax
python -c "import yaml; from pathlib import Path; \
[print(f'✓ {f.stem}') for f in Path('kb/model_cards').glob('*.yaml') \
if f.stem != 'template' and yaml.safe_load(f.read_text())]"

# Codex gate (fast / full)
python scripts/codex_gate.py --mode fast --label cycle1 --since origin/main
python scripts/codex_gate.py --mode full --label cycle2 --since HEAD~1
```

### PDF Converter

```bash
# Navigate to PDF repo
cd ~/Projects/pdf\<-\>md\;ai-summaries

# Install dependencies
pip install -r requirements.txt

# Convert PDF to Markdown
python pdf_to_markdown.py paper.pdf output.md

# Generate AI summary
python summary_generator.py paper.md summary.md

# Convert to aesthetic PDF
python markdown_to_pdf.py summary.md output.pdf

# Full pipeline
python pdf_to_markdown.py paper.pdf paper.md && \
python summary_generator.py paper.md summary.md && \
python markdown_to_pdf.py summary.md summary.pdf
```

---

## 📊 Repository Stats

### Neurogenomics-KB (Updated Nov 18, 2025)
- **Code Walkthroughs**: 9 complete guides (with KB reference links)
- **Model Cards**: 9 validated YAML files
- **Paper Cards**: 12 structured cards (NEW ✨)
- **Dataset Cards**: 11 specifications + UKB manifest stub (NEW ✨)
- **Integration Cards**: 2 multimodal strategies
- **Experiment Configs**: 3 ready-to-run templates (NEW ✨)
- **External Repos**: 7 reference implementations

### PDF Converter
- **Scripts**: 3 Python tools
- **Features**: PDF↔MD conversion, AI summarization, aesthetic PDFs
- **Theme**: Baby blue, lavender, wine red

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

  > “You are part of a team of domain agents (brain, genetics, integration, scripts, master).  
  > In **your own domain slice**, update any relevant docs and KB cards so that the description and usage of the UKB fMRI and genetics datasets are consistent across model cards, dataset cards, and walkthroughs.  
  > Do not edit files that are clearly outside your domain. At the end, summarize exactly which files you changed and why.”

- **Master coherence pass example**:

  > “Act as the **Global master / coherence agent**.  
  > Read across the project to check naming and conceptual consistency between brain and genetics sections.  
  > You may only edit: README, ORGANIZATION_SUMMARY, QUICK_REFERENCE, TREE_VIEW, docs index/integration docs, KB section READMEs, and the integration cards for genetics embeddings and UKB alignment.  
  > Propose and apply small edits to those meta files so they accurately describe the current structure and relationships in the KB.”

- **Domain-specific update example (brain only)**:

  > “Consider only **brain-related** docs, walkthroughs, model cards, and datasets.  
  > Bring BrainMT and BrainLM docs + cards into alignment with the `hcp_fmri_tensor` and `ukb_fmri_tensor` dataset cards, updating only brain files.  
  > Do not modify genetics or non-brain content.”

---

## ✅ What's Clean

- ✅ No implementation scripts in KB repo
- ✅ All YAML cards parse successfully
- ✅ Generator walkthrough fixed (was empty)
- ✅ README clarified (KB-only purpose)
- ✅ PDF tools moved to separate repo
- ✅ All walkthroughs complete

---

## 🎨 PDF Converter Features

**Color Scheme:**
- Baby Blue (#89CFF0) - Main headers
- Lavender (#B695C0) - Subheaders
- Wine Red (#722F37) - Accents
- Times New Roman - Body font

**Capabilities:**
- PDF → Markdown with structure detection
- Markdown → PDF with professional styling
- AI-powered summary extraction (key points, methods, results, limitations)

---

## 📝 Next Steps

### For Neurogenomics-KB:
1. Continue documenting models and integration strategies
2. Add paper cards to `kb/paper_cards/`
3. Expand integration playbooks in `docs/integration/`
4. Keep YAML cards updated with new checkpoints

### For PDF Converter:
1. Push to GitHub: `cd ~/Projects/pdf<->md;ai-summaries && git push`
2. Test with your research papers
3. Customize colors if desired (edit `markdown_to_pdf.py`)

---

## 🔗 Quick Links

### Documentation
- **Main KB Index**: `docs/index.md`
- **Code Walkthroughs**: `docs/code_walkthroughs/`
- **Integration Strategy**: `docs/integration/integration_strategy.md`
- **Analysis Recipes**: `docs/integration/analysis_recipes/`
- **Integration Plan**: `docs/decisions/2025-11-integration-plan.md`

### Cards
- **Model Cards**: `kb/model_cards/`
- **Paper Cards**: `kb/paper_cards/` (NEW ✨)
- **Dataset Cards**: `kb/datasets/`
- **Integration Cards**: `kb/integration_cards/`

### Configs & Tools
- **Experiment Configs**: `configs/experiments/` (NEW ✨)
- **KB Script**: `scripts/manage_kb.py`
- **PDF Tools**: `~/Projects/pdf<->md;ai-summaries/`

### Summaries
- **KB Completion**: `KB_COMPLETION_SUMMARY.md` (NEW ✨)
- **Organization**: `ORGANIZATION_SUMMARY.md`

---

**Last Updated**: November 17, 2025  
**Organized by**: Allison Eun Se You  
**Status**: ✅ Nov 21 KB Complete — Ready for Nov 26 baselines

