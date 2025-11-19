# KB Results Layout

This directory documents how analysis results **should** be organized and recorded for experiments that
use the configurations and strategies defined in this KB. Actual result files may live in separate
analysis repositories or storage locations; this README defines the canonical layout and metadata.

## Directory structure (suggested)

- `results/`
  - `YYYY-MM-DD_<exp_id>/`
    - `config_used.yaml`        # frozen copy of the experiment config
    - `metrics_summary.yaml`    # top-level metrics (means, SDs, CIs)
    - `per_fold_metrics.csv`    # fold-wise metrics for statistical tests
    - `artifacts/`              # plots, tables, logs

## Required metadata fields

Each `metrics_summary.yaml` should include at minimum:

- `exp_id`: experiment identifier (e.g., `01_cca_gene_smri`, `dev_01_brain_only_baseline`).
- `dataset_ids`: list of dataset cards used (e.g., `["ukb_wes", "ukb_smri_freesurfer"]`).
- `embedding_strategies`: list of strategy IDs used.
- `manifest_id`: subject manifest card, if applicable.
- `metrics`: dictionary of primary metrics (AUROC, AUPRC, canonical correlations, etc.).
- `run_date`: ISO date.

## Policy

- Results stored here are **summaries and metadata**, not raw data.
- Any subject-level predictions or embeddings should live in governed analysis storage, not in this KB.
- When in doubt, err on the side of keeping PHI/row-level outputs **out** of this repository and recording
  only the aggregate statistics and configuration references.


