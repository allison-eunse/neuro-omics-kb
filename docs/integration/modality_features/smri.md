---
title: Modality Features — sMRI
status: ready
updated: 2025-11-18
---

# sMRI Features

## Baseline embedding (`smri_free_surfer_pca512_v1`)

- Input: FreeSurfer 7.x `aparc.stats` (thickness + volume) + `aseg.stats` (~176 ROIs).
- Fold discipline:
  - Train-fold z-score per feature.
  - Residualize covariates: age, sex, site/scanner, intracranial volume (±SES).
- Dimensionality: PCA → 512-D subject vector (fit on train fold, apply to train/test).
- Harmonization hooks: default `none_baseline`; optional `combat_smri` or `murd_t1_t2` before FreeSurfer (see `kb/integration_cards/harmonization_methods.yaml`).
- Reference the recipe via `python scripts/manage_kb.py ops strategy smri_free_surfer_pca512_v1` and log the ID inside experiment configs.

## Future extensions to log as new strategies

- **sMRI FM encoders.** Whole-volume ViTs or hub-token encoders (Brain Harmony Stage 0) that emit subject embeddings directly; register as `smri_fm_encoder_*`.
- **Diffusion MRI.** Tract-based spatial stats or tractography metrics → z-score → residualize → PCA→512.
- **Tabular predictors.** When skipping PCA (raw 176-D features), reference `smri_free_surfer_raw_176` and evaluate TabPFN vs. LR/GBDT for tabular baselines.

Always pair sMRI embeddings with consistent covariates and document which harmonization method (if any) preceded ROI extraction.
