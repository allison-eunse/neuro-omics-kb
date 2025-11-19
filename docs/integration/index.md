# Integration Hub

Everything in this section supports the late-fusion-first plan documented in the decision log. Use it as the connective tissue between per-modality preprocessing, harmonization, and experiment execution.

- **Strategy.** The high-level playbook: covariates to regress, projection dims, when to escalate beyond late fusion.
- **Analysis recipes.** Copy-ready runbooks for CCA + permutation, prediction baselines, and partial correlations.
- **Modality specs.** Concrete instructions for genomics, sMRI, and rs-fMRI features, each pointing to the canonical `embedding_strategies.<id>`.
- **Design patterns & benchmarks.** Reusable integration motifs plus prior benchmark targets to compare against.

Before running anything, grab the relevant IDs via `python scripts/manage_kb.py ops strategy …` and `python scripts/manage_kb.py ops harmonization …`, then log them with your CV fold definitions. This keeps downstream reports auditable even when raw datasets (e.g., UKB) cannot be shared.