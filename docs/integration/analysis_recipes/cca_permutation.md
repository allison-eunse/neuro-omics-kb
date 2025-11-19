---
title: Analysis Recipe — CCA + Permutation
status: ready
updated: 2025-11-18
---

# CCA + Permutation

Inputs

- X_gene, X_brain: residualized and standardized matrices (N × d_gene, N × d_brain) projected to ~512 dims.
- Covariates: used upstream during residualization.
- Metadata: record `embedding_strategies.<id>`, `harmonization_methods.<id>`, and (for fMRI) `rsfmri_preprocessing_pipelines.<id>` to ensure results are traceable.

Context in integration plan

- This recipe is part of the **diagnostic / exploration layer** of the integration stack.
- Run it **after per-modality sanity checks** but before heavier fusion models; it tells you whether there is cross-modal structure worth chasing.
- Treat it as a companion to the late-fusion-first baselines rather than a replacement for prediction experiments.

Protocol

1) Fold discipline
- Use K stratified folds (group/site-aware if needed).
- Within each train fold:
  - Fit CCA on X_gene_train, X_brain_train.
  - Transform train and test to canonical scores.
2) Permutation
- For b in 1..B (B = 1,000):
  - Permute subject alignment in one modality within the train fold.
  - Fit CCA on permuted pairs.
  - Record ρ1_null.
- p = (count(ρ1_null ≥ ρ1_obs) + 1) / (B + 1).
3) Reporting
- ρ1–ρ3 with permutation p-values.
- Optional: bootstrap CIs on ρ1.
- Loadings/feature contributions for interpretation.

Why pair CCA with permutations?

- CCA will always produce non-zero canonical correlations—even when there is no shared structure—because it can overfit high-dimensional spaces.
- The permutation loop builds a modality-shuffled null distribution so we can report p-values (or FDR-adjusted thresholds) and avoid over-interpreting noise.
- This statistical check is lightweight enough for “quick tests” while still respecting site/ancestry confounds.

Pitfalls
- Never fit CCA on all data.
- Keep the same permutation protocol across folds for comparability.
