---
title: Embedding policies
status: draft
updated: 2025-11-19
---

## Embedding naming and PCA policies

This page documents how we name embedding strategies in `kb/integration_cards/embedding_strategies.yaml` and how
we choose PCA dimensionality before locking in a strategy ID.

### Naming conventions

- **UKB sMRI PCA embeddings**
  - `smri_ukb_pca32_v1`, `smri_ukb_pca64_v1`, `smri_ukb_pca128_v1`, `smri_ukb_pca256_v1`
  - All refer to PCA-compressed FreeSurfer ROI features from `ukb_smri_freesurfer.yaml`, differing only in `dim`.

- **CHA developmental sMRI PCA embeddings**
  - `smri_cha_dev_pca64_v1`, `smri_cha_dev_pca128_v1`
  - Both wrap the same preprocessing pipeline (age/sex adjustment, pediatric QC) on `cha_dev_longitudinal.yaml`,
    differing only in PCA `dim`.

- **Genetics / Joo embeddings**
  - `genetics_gene_fm_pca512_v1`: generic gene-FM PCA embedding for adult UKB.
  - `genetics_joo_mdd_cog_v1`: Prof. Joo MDD + cognition gene embeddings (Yoon BIOKDD'25-style); dimension and FM
    backbone to be filled once confirmed.

In general:

- Start IDs with the **modality** (`smri_`, `rsfmri_`, `eeg_`, `genetics_`, `behaviour_`).
- Follow with the **cohort** or context (`ukb`, `cha_dev`, etc.).
- Then append the **method** and key hyperparameters (`pca64`, `pca128`, `pgs20traits`, etc.).
- End with a monotonically increasing **version suffix** (`_v1`, `_v2`, …).

### PCA dimensionality policy

When choosing PCA dims for new strategies (especially sMRI):

1. **Upper bound**  
   - Let \(p\) = number of input features (e.g., ≈176 sMRI ROIs) and \(n\) = usable subjects.  
   - Do not set `dim > p`, and keep `dim ≪ n` (e.g., ≤ n/2) to avoid unstable components.

2. **Variance explained check (one-off)**  
   - On a representative training fold, fit PCA and inspect the cumulative variance curve.
   - Record dims where cumulative variance hits ~70, 80, 90% (e.g., 64, 128, 256).

3. **Grid search with nested CV**  
   - Define a small grid:
     - UKB sMRI: `[32, 64, 128, 256]` → registered as `smri_ukb_pca32_v1`…`pca256_v1`.
     - CHA sMRI: `[64, 128]` (given smaller N and higher heterogeneity).
   - Run nested CV for the **actual downstream task** (prediction or CCA+permutation) and compare dims by:
     - AUROC/AUPRC for classifiers, or
     - significance and stability of canonical correlations for CCA.
   - Choose the **smallest dim within the 1 SE band** of the best-performing dim, and record that as the default.

4. **Hardening the choice**
   - Once a dim is selected, promote that strategy ID (e.g., `smri_ukb_pca128_v1`) as the **default** in downstream
     experiment configs and document the decision (date, grid, metric) in results/metadata.

### Policy summary

- **Rule of thumb**: start with `dim = min(128, p, n/2)` and adjust via nested CV.
- Never change the definition of an existing `*_v1` strategy silently; instead, create `_v2` and link to the decision.
- Always tie a strategy ID back to:
  - a dataset card (`kb/datasets/*.yaml`),
  - a preprocessing description (this page + modality-specific docs), and
  - at least one experiment config that demonstrates its use.


