---
title: Modality Features — fMRI
status: ready
updated: 2025-11-18
---

# fMRI Features

## Reference preprocessing stacks

- Cataloged in `kb/integration_cards/rsfmri_preprocessing_pipelines.yaml`. Default: `hcp_like_minimal` (motion + distortion correction, nuisance regression, 0.01–0.1 Hz filter, Schaefer-400 parcellation).
- Document which pipeline ID you used per run; experiments reference it alongside the embedding strategy ID.

## Subject-level embedding strategies

- `rsfmri_swift_segments_v1` (SwiFT):
  - 20-frame segments → mean-pool tokens from the last hidden state → mean over segments per run → mean over runs per subject.
  - Fold-wise z-score + residualize(age, sex, site/scanner, mean FD, DVARS) → PCA→512.
  - Source references: `docs/code_walkthroughs/swift_walkthrough.md`.
- `rsfmri_brainlm_segments_v1` (BrainLM ViT-MAE):
  - 32-frame windows with stride 16 → CLS pooling per window → attention pooling across windows with inverse-FD weights → mean over runs.
  - Fold-wise z-score + residualize(age, sex, site, FD, DVARS) → PCA→512.
- `rsfmri_brainjepa_roi_v1` (Brain-JEPA):
  - ROI tokens (Schaefer-400 + Tian-50) → mean pooling across unmasked tokens → option to average per functional network → subject mean.
  - Residualize age/sex/site/motion (optionally GSR flag) → PCA→512.
- `rsfmri_brainmt_segments_v1` (BrainMT):
  - 32-frame conv/Mamba segments → mean patch tokens per segment → run mean → subject mean.
  - Residualize age/sex/site/motion → PCA→512.

All recipes live in `kb/integration_cards/embedding_strategies.yaml`; call `python scripts/manage_kb.py ops strategy <id>` to print the full pipeline (including preprocessing notes and sources) before launching extraction.

## Classical atlas baseline (optional)

- For quick sanity checks, you can still run atlas-based functional connectivity:
  - Schaefer-400 time courses → Pearson FC matrix → Fisher z → vectorize upper triangle → z-score/residualize (include motion/site covariates) → PCA to 100–256 → optionally pad to 512.
  - Track this by creating its own `embedding_strategies` entry if you plan to use it beyond ad-hoc QA.
