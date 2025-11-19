---
title: Neurogenomics KB
status: draft
updated: 2025-11-18
---

# Neurogenomics Knowledge Base

This KB captures the design rationale, integration strategy, and reproducible analysis recipes that connect **genomics, brain, and behavioural representations** across both **adult** and **developmental / neurodevelopmental** cohorts. It started from **adult UK Biobank–centric gene–brain FM alignment** (genetics FM + MRI-derived features) and now extends to **longitudinal, multimodal gene–brain–behaviour FMs**, including MRI/fMRI Brain FMs, EEG/EPhys FMs, genetics / multi-omics FMs, and clinical / cognitive / developmental assessments.

> Maintained by Allison Eun Se You

!!! tip "New here?"
    Start with the [KB overview](guide/kb_overview.md) for a map of the architecture, registry IDs, and run-logging expectations.

## Decisions & roadmaps

- [Integration baseline plan (Nov 2025)](decisions/2025-11-integration-plan.md) — late fusion first, then escalate if fusion wins.

## Integration stack

- **Integration strategy:** [integration/integration_strategy.md](integration/integration_strategy.md)
- **Analysis recipes:**
  - [CCA + permutation](integration/analysis_recipes/cca_permutation.md)
  - [Prediction baselines](integration/analysis_recipes/prediction_baselines.md)
  - [Partial correlations](integration/analysis_recipes/partial_correlations.md)
- **Modality features:**
  - [Genomics](integration/modality_features/genomics.md)
  - [sMRI](integration/modality_features/smri.md)
  - [fMRI](integration/modality_features/fmri.md)
  - (Planned) EEG/EPhys and developmental / behavioural feature specs for longitudinal cohorts.

## Model guides

- **Brain FMs:** [BrainLM](models/brain/brainlm.md), [Brain-JEPA](models/brain/brainjepa.md), [Brain Harmony](models/brain/brainharmony.md), [SwiFT](models/brain/swift.md), [BrainMT](models/brain/brainmt.md)
- **Genetics FMs:** [Caduceus](models/genetics/caduceus.md), [DNABERT-2](models/genetics/dnabert2.md), [Evo2](models/genetics/evo2.md), [GENERator](models/genetics/generator.md)
- **Multimodal / Clinical FMs:** Walkthroughs + YAML cards for [M3FM](code_walkthroughs/m3fm_walkthrough.md) (`kb/model_cards/m3fm.yaml`), [Me-LLaMA](code_walkthroughs/melamma_walkthrough.md) (`kb/model_cards/me_llama.yaml`), and [TITAN](code_walkthroughs/titan_walkthrough.md) (`kb/model_cards/titan.yaml`) now appear in the registry and dashboards.
- **Survey / reference catalog:** `kb/datasets/fms_medical_catalog.yaml` captures the bilingual “Awesome Foundation Models for Advancing Healthcare” list surfaced in [the new walkthrough](code_walkthroughs/fms_medical_walkthrough.md).
- **Tabular FM:** `kb/model_cards/tabpfn.yaml` — Primary paper [Nature (2025)](https://www.nature.com/articles/s41586-024-08328-6) · code [PriorLabs/TabPFN](https://github.com/PriorLabs/TabPFN)

## Data references

- **Governance & QC:** [data/governance_qc.md](data/governance_qc.md)
- **UKB data map & schemas:** [data/ukb_data_map.md](data/ukb_data_map.md)
- **Dataset manifest:** `kb/datasets/ukb_manifest_stub.yaml` (in-repo path; not published)
- **Curated external catalogs:** `kb/datasets/fms_medical_catalog.yaml` for the Awesome Foundation Models roundup (paired with [docs/code_walkthroughs/fms_medical_walkthrough.md](code_walkthroughs/fms_medical_walkthrough.md)).
- (Planned) Developmental / neurodevelopmental cohort cards (e.g., Cha Hospital longitudinal cohort) capturing visit structure, diagnostic composition, and modality inventory.

## KB assets (YAML + curated sources)

- **Model cards:** `kb/model_cards/`
- **Paper cards:** `kb/paper_cards/`
- **Integration principles / curated notes:** `docs/generated/kb_curated/integration_cards/`
- **Dataset cards:** `kb/datasets/`
- **Paper source files:** `docs/generated/kb_curated/papers-md/` (markdown summaries) and `docs/generated/kb_curated/papers-pdf/` (original PDFs from `pdf<->md;ai-summaries`). Keep both as the citation backbone for YAML updates.
- (Planned) Semantic alignment / hub cards describing how gene, brain, EEG, and behavioural embeddings are aligned to **LLM** and **VLM** spaces in ARPA-H–style Brain-Omics Model (BOM) projects.

## Experiment configs

- Templates in `configs/experiments/` — NEW ✨

## Quick start

- **Baselines**
  - Z-score → residualize → per-modality 512-D projection → CCA + permutations → LR/GBDT (Gene, Brain, Fusion) → DeLong/bootstrap
- **Confounds**
  - Age, sex, site/scanner, motion (FD), SES, genetic PCs
- **Roadmap**
  - Late fusion first → two-tower contrastive → EI stacking → hub tokens/TAPE if needed
- **Quick test**
  - Run the CCA + permutation template first; it surfaces cross-modal structure before heavier prediction/fusion experiments.

Pairing CCA with permutation:

CCA alone will always return non-zero canonical correlations, even on shuffled data. The permutation loop builds a null distribution (re-fitting CCA after shuffling one modality within the train fold) so we can report p-values and avoid over-interpreting noise—critical when cohorts share confounds like site or ancestry.

## KB workflow

### Paper cards (NEW ✨)
All 12 papers from `pdf<->md;ai-summaries/input/` now have structured YAML cards in `kb/paper_cards/`:

??? note "Paper card index"
    **Integration principles:**

    - `kb/paper_cards/ensemble_integration_li2022.yaml` — Late fusion rationale ([PDF](generated/kb_curated/papers-pdf/ensemble_integration_li2022.pdf))
    - `kb/paper_cards/oncology_multimodal_waqas2024.yaml` — Confounds & evaluation ([PDF](generated/kb_curated/papers-pdf/oncology_multimodal_waqas2024.pdf))

    **Foundation models:**

    - `kb/paper_cards/caduceus_2024.yaml` — RC-equivariant DNA FM ([PDF](generated/kb_curated/papers-pdf/caduceus_2024.pdf))
    - `kb/paper_cards/evo2_2024.yaml` — 1M context StripedHyena ([PDF](generated/kb_curated/papers-pdf/evo2_2024.pdf))
    - `kb/paper_cards/generator_2024.yaml` — 6-mer generative DNA LM ([PDF](generated/kb_curated/papers-pdf/generator_2024.pdf))
    - `kb/paper_cards/brainlm_2024.yaml` — ViT-MAE for fMRI ([PDF](generated/kb_curated/papers-pdf/brainlm_2024.pdf))
    - `kb/paper_cards/brainjepa_2024.yaml` — JEPA for fMRI ([PDF](generated/kb_curated/papers-pdf/brainjepa_2024.pdf))
    - `kb/paper_cards/brainharmony_2025.yaml` — sMRI+fMRI with TAPE ([PDF](generated/kb_curated/papers-pdf/brainharmony_2025.pdf))
    - `kb/paper_cards/brainmt_2025.yaml` — Hybrid Mamba-Transformer ([PDF](generated/kb_curated/papers-pdf/brainmt_2025.pdf))

    **Methods & prior work:**

    - `kb/paper_cards/yoon_biokdd2025.yaml` — MDD gene embeddings + LOGO ([PDF](generated/kb_curated/papers-pdf/yoon_biokdd2025.pdf))
    - `kb/paper_cards/prs_guide.yaml` — Polygenic risk scores ([PDF](generated/kb_curated/papers-pdf/prs_guide.pdf))
    - `kb/paper_cards/gwas_diverse_populations.yaml` — Ancestry control ([PDF](generated/kb_curated/papers-pdf/gwas_diverse_populations.pdf))

### Experiment configs (NEW ✨)
Ready-to-run YAML templates live in `configs/experiments/`:

- `01_cca_gene_smri.yaml` — CCA + permutation baseline
- `02_prediction_baselines.yaml` — Gene vs sMRI vs Fusion
- `03_logo_gene_attribution.yaml` — LOGO ΔAUC protocol

### Integration cards

Drop new evidence into `docs/generated/kb_curated/integration_cards/` (run `pdf<->md;ai-summaries/build_docs.sh` after curating).

### Usage
1. Read paper card YAML for context
2. Check linked code walkthrough for implementation
3. Clone experiment config template
4. Fill dataset paths and parameters
5. Run and log outputs back to KB
