# Integration Hub

Everything in this section supports the **phased escalation strategy** documented in the [Integration Plan (Nov 2025)](../decisions/2025-11-integration-plan/). Use it as the connective tissue between per-modality preprocessing, harmonization, and experiment execution.

## Overview

This hub provides **end-to-end guidance** for integrating genetics, brain, and behavioral data using foundation models.

### 📋 Key Resources

- **[Integration Strategy](integration_strategy/)** — High-level playbook: covariates to regress, projection dims, escalation triggers
- **[Design Patterns](design_patterns/)** — Late fusion → two-tower → MoT → BOM escalation logic
- **[Multimodal Architectures](multimodal_architectures/)** — Detailed patterns from BAGEL, MoT, M3FM, Me-LLaMA, TITAN
- **[Embedding Policies](embedding_policies/)** — Naming conventions and PCA dimensionality guidelines
- **[Benchmarks](benchmarks/)** — Prior benchmark targets to compare against

### 🔬 Analysis Recipes

Copy-ready runbooks for common integration tasks:

- **[CCA + Permutation](analysis_recipes/cca_permutation/)** — Test gene-brain associations before heavy fusion
- **[Prediction Baselines](analysis_recipes/prediction_baselines/)** — Gene-only vs Brain-only vs Late fusion
- **[Partial Correlations](analysis_recipes/partial_correlations/)** — Control for covariates with logistic regression

### 🧬🧠 Modality Features

Concrete instructions for extracting and harmonizing features:

- **[Genomics](modality_features/genomics/)** — Genetics embeddings, RC-equivariance, gene attribution
- **[sMRI](modality_features/smri/)** — FreeSurfer ROIs, PCA compression, site harmonization
- **[fMRI](modality_features/fmri/)** — Functional connectivity, BrainLM/SwiFT embeddings, preprocessing

### 🎨 Integration Cards

Comprehensive multimodal fusion guidance:

- **[Ensemble Integration](../models/integrations/ensemble_integration/)** — Model stacking, averaging, meta-learning
- **[Oncology Multimodal Review](../models/integrations/oncology_multimodal_review/)** — Early/intermediate/late fusion taxonomy
- **[Multimodal FM Patterns](../models/integrations/multimodal_fm_patterns/)** — Architectural patterns from state-of-the-art FMs

## Quick Start

**Before running any analysis**, grab the relevant strategy IDs and log them with your experiment configs:

```bash
# Show sMRI baseline recipe
python scripts/manage_kb.py ops strategy smri_free_surfer_pca512_v1

# Inspect harmonization metadata (e.g., MURD)
python scripts/manage_kb.py ops harmonization murd_t1_t2

# Show rs-fMRI preprocessing stack
python scripts/manage_kb.py ops strategy rsfmri_swift_segments_v1
```

This keeps downstream reports **auditable** even when raw datasets (e.g., UKB) cannot be shared.

## Integration Phases

We follow a **phased escalation strategy** to avoid premature complexity:

| Phase | Status | Pattern | Trigger | Documentation |
|-------|--------|---------|---------|---------------|
| **Phase 1** | ✅ Active | Late Fusion | Baseline | [Integration Plan](../decisions/2025-11-integration-plan/#phase-1-late-fusion-baselines-current) |
| **Phase 2** | 🚧 Prep | Two-Tower Contrastive | CCA p<0.001, ΔAUROC>5% | [Integration Plan](../decisions/2025-11-integration-plan/#phase-2-two-tower-contrastive-near-term) |
| **Phase 3** | ⏳ Future | Unified Multimodal (MoT/BAGEL/LLM-Bridge) | ΔAUROC>10%, cross-modal reasoning | [Integration Plan](../decisions/2025-11-integration-plan/#phase-3-unified-multimodal-architectures-long-term) |

## Navigation Guide

### For Late Fusion Workflows (Phase 1)

1. Read [Integration Strategy](integration_strategy/)
2. Pick analysis recipe: [CCA](analysis_recipes/cca_permutation/), [Prediction](analysis_recipes/prediction_baselines/), or [Partial Correlations](analysis_recipes/partial_correlations/)
3. Extract features: [Genomics](modality_features/genomics/), [sMRI](modality_features/smri/), [fMRI](modality_features/fmri/)
4. Review [Ensemble Integration](../models/integrations/ensemble_integration/) card for stacking strategies
5. Run analysis with logged strategy IDs

### For Multimodal Architecture Design (Phase 2+)

1. Read [Design Patterns](design_patterns/) for escalation logic
2. Study [Multimodal Architectures](multimodal_architectures/) for BAGEL/MoT/M3FM/Me-LLaMA/TITAN patterns
3. Review [Multimodal FM Patterns](../models/integrations/multimodal_fm_patterns/) integration card
4. Consult [Oncology Multimodal Review](../models/integrations/oncology_multimodal_review/) for fusion taxonomy
5. Check [Integration Plan](../decisions/2025-11-integration-plan/) decision table for recommended pattern

### For Adding New Integration Strategies

1. Start from [Integration card template](../models/integrations/template/)
2. Review existing cards for structure and style
3. Document mechanics, use cases, caveats, and BOM integration
4. Add to `models/integrations/` directory
5. Update `mkdocs.yml` navigation

## Key Principles

✅ **Late fusion first** — Preserve modality-specific signal under heterogeneous semantics  
✅ **Unimodal baselines** — Establish gene-only and brain-only performance before multimodal claims  
✅ **Covariate control** — Z-score + residualize vs age/sex/site before interpreting effects  
✅ **Reproducibility** — Log embedding strategy IDs, harmonization methods, CV folds  
✅ **Phased escalation** — Only escalate when data and compute justify the complexity  

[Read full integration plan →](../decisions/2025-11-integration-plan/)