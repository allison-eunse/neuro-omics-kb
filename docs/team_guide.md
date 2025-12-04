---
title: Team User Guide
updated: 2025-12-04
---

# 🧬🧠 Team User Guide

**For:** Lab members working on Brain–Genetics FM integration

!!! tip "Quick Start for New Team Members"
    1. Read this guide (you're here!)
    2. Browse the [Integration Strategy](integration/integration_strategy.md)
    3. Check [experiment configs](https://github.com/allison-eunse/neuro-omics-kb/tree/main/configs/experiments)

---

## 🎯 What This Repo Does

This is your **documentation-first knowledge base** — the map and spec for the Brain–Genetics program.

**It centralizes:**

### 1. **Model Knowledge** (20 FMs)
- **Genetics FMs:** Caduceus, DNABERT-2, Evo 2, HyenaDNA, GENERator
- **Brain FMs:** BrainLM, Brain-JEPA, BrainMT, Brain Harmony, SwiFT  
- **Multimodal FMs:** BAGEL, MoT, M3FM, Me-LLaMA, TITAN, Flamingo, FMS-Medical

Each has: YAML card + walkthrough + documentation

### 2. **Paper Knowledge** (30 papers)
- RC symmetry/consistency
- Ensemble integration (EI)
- MURD harmonization, site-unlearning
- Multimodal FM surveys
- Yoon BioKDD'25 (LOGO attribution)

### 3. **Integration Knowledge**
**THE PLAYBOOK:** `docs/integration/integration_strategy.md`

**Strategy:** Late fusion → two-tower contrastive → MoT/unified BOM (escalate only if justified)

### 4. **Experimental Playbook**
Ready-to-run configs in `configs/experiments/`:
- CCA + permutation
- Prediction baselines (Gene vs Brain vs Fusion)
- LOGO attribution

---

## 📋 Canonical Embedding Recipes

!!! info "All recipes defined in `kb/integration_cards/embedding_strategies.yaml`"
    Query any recipe: `python scripts/manage_kb.py ops strategy <recipe_id>`

| Recipe ID | Modality | What It Does |
|:----------|:--------:|:-------------|
| `genetics_gene_fm_pca512_v1` | 🧬 Genetics | Caduceus/DNABERT-2/Evo2 + RC-averaging → 512-D |
| `genetics_joo_mdd_cog_v1` | 🧬 Genetics | **Prof. Joo's 38 MDD genes pipeline** |
| `smri_free_surfer_pca512_v1` | 🧠 sMRI | FreeSurfer ROIs → residualize → PCA→512 |
| `rsfmri_swift_segments_v1` | 🧠 fMRI | SwiFT embeddings → PCA→512 |
| `rsfmri_brainlm_segments_v1` | 🧠 fMRI | BrainLM embeddings → PCA→512 |
| `fusion_concat_gene_brain_1024_v1` | 🔗 Fusion | Concat(Gene₅₁₂, Brain₅₁₂) → 1024-D |

**Query a recipe:**
```bash
python scripts/manage_kb.py ops strategy genetics_joo_mdd_cog_v1
```

---

## 🗺️ How to Navigate

### → "I need to understand a specific FM"

!!! example "Example: Understanding Caduceus"
    1. **Overview:** [Caduceus model docs](models/genetics/caduceus.md)
    2. **Step-by-step:** [Caduceus walkthrough](code_walkthroughs/caduceus_walkthrough.md)
    3. **Code:** `external_repos/caduceus/`
    4. **Metadata:** `kb/model_cards/caduceus.yaml`

### → "I want to run CCA / prediction baselines"

1. **Read the playbook:** `docs/integration/integration_strategy.md`
2. **Check the recipe:** `kb/integration_cards/embedding_strategies.yaml`
3. **Use the config:** `configs/experiments/01_cca_gene_smri.yaml` or `02_prediction_baselines.yaml`

### → "How do I preprocess [modality]?"

- **Genetics:** `docs/integration/modality_features/genomics.md`
- **sMRI:** `docs/integration/modality_features/smri.md`
- **fMRI:** `docs/integration/modality_features/fmri.md`

### → "Which harmonization method?"

```bash
python scripts/manage_kb.py ops harmonization murd_t1_t2
```

Or read: `docs/integration/integration_strategy.md` (Harmonization section)

---

## 🚀 Your Jan-Feb Action Plan

!!! success "Meeting Goals: Jan-Feb Wrap-Up"
    - Test with 20-participant toy sample
    - Use new NVIDIA Spark GPU (128GB)  
    - Offline genetics embeddings from Prof. Joo
    - Brain features (fMRI parcellation available)
    - Complete Stage-1 baselines

### **Week 1-2: Small Sample Testing (20 participants)**

**Goal:** Test pipeline on toy sample using new NVIDIA Spark GPU (128GB)

```bash
# 1. Download 20-participant sample
#    - Brain features (fMRI parcellation available now)
#    - Genomics embeddings from Prof. Joo (offline, already trained)

# 2. Test embedding extraction
python scripts/manage_kb.py ops strategy genetics_joo_mdd_cog_v1

# 3. Run on NVIDIA Spark GPU
# 4. Verify pipelines work end-to-end
```

**What to test:**
- Brain feature download works
- Genomics embeddings load correctly
- CCA runs without errors
- Prediction baselines produce AUROCs

### **Week 3-4: Run Stage-1 Experiments**

**Goal:** Gene ↔ Brain correlation + prediction baselines

**Use these configs:**
1. `configs/experiments/01_cca_gene_smri.yaml`
   - Gene ↔ sMRI CCA + 1,000 permutations
   - Check if ρ₁–ρ₃ are significant (p < 0.05)

2. `configs/experiments/02_prediction_baselines.yaml`
   - Gene-only → MDD
   - Brain-only → MDD  
   - Fusion (Gene+Brain) → MDD
   - DeLong test: Is Fusion > max(Gene, Brain)?

3. Document results in `kb/results/`

### **Week 5-8: Decide on Escalation**

**Decision criteria:**

| Result | Next Action |
|--------|-------------|
| `Fusion > max(Gene, Brain)` p < 0.05 | → Consider two-tower contrastive |
| `Fusion ≈ best single modality` | → Focus on improving per-modality models |
| CCA strong (ρ₁ > 0.3, p < 0.001) | → Supports two-tower alignment |

**Templates available:**
- Two-tower patterns: `docs/integration/design_patterns.md`
- MoT/BAGEL patterns: `docs/integration/multimodal_architectures.md`

---

## 🧪 What You Can Do Right Now (Before Data)

### ✅ Available Now

1. **Read model walkthroughs** — Understand how each FM works
2. **Study embedding recipes** — Know what preprocessing to apply
3. **Review experiment configs** — Understand analysis pipeline
4. **Validate YAML cards** — `python scripts/manage_kb.py validate models`
5. **Clone external repos** — Familiarize with FM codebases

### 🟡 Waiting For

- **UKB data access approval** (fMRI/sMRI features)
- **Genetics embeddings** from Prof. Joo's team
- **Cha Hospital developmental cohort** (future)

### 📚 Onboarding New Team Members

**Recommended reading order:**
1. This guide (TEAM_GUIDE.md)
2. `README.md` — High-level overview
3. `docs/integration/integration_strategy.md` — THE PLAYBOOK
4. `configs/experiments/01_cca_gene_smri.yaml` — See what we're running
5. Pick one FM walkthrough to read in detail

---

## 🔬 Stage-1 Experiments (Your Current Focus)

!!! abstract "Experiment 1: CCA (Gene ↔ Brain Association)"
    **Config:** `configs/experiments/01_cca_gene_smri.yaml`
    
    **What it does:**
    
    - Tests if gene embeddings share structure with brain embeddings
    - 1,000 permutations to assess significance
    - Reports ρ₁–ρ₃ (canonical correlations) with p-values
    
    **Success criteria:**
    
    - ρ₁ > 0.2 with p < 0.05 → significant association
    - Gene/ROI loadings interpretable

!!! abstract "Experiment 2: Prediction (Gene vs Brain vs Fusion)"
    **Config:** `configs/experiments/02_prediction_baselines.yaml`
    
    **What it does:**
    
    - Compares 3 baselines for MDD prediction:
        - Gene-only (512-D)
        - Brain-only (512-D)
        - Fusion (1024-D concatenation)
    - Uses LR + LightGBM + CatBoost
    - DeLong test to compare AUROCs
    
    **Success criteria:**
    
    - If Fusion > max(Gene, Brain) p < 0.05 → integration adds value
    - Document which modality is stronger

!!! abstract "Experiment 3: LOGO Attribution"
    **Config:** `configs/experiments/03_logo_gene_attribution.yaml`
    
    **What it does:**
    
    - Leave-one-gene-out ΔAUC
    - Identifies which genes contribute most to prediction
    - Wilcoxon test + FDR correction
    
    **Success criteria:**
    
    - Find significant genes (p < 0.05 FDR-corrected)
    - Compare with literature (SOD2, HOXA10, etc.)

---

## 🚦 Escalation Decision Tree

```
Start: Run Stage-1 (CCA + Prediction + LOGO)
  │
  ├─ Fusion > single-modality (p < 0.05)?
  │  │
  │  ├─ YES → CCA also significant?
  │  │  │
  │  │  ├─ YES → Consider two-tower contrastive
  │  │  │        (frozen FMs + small projectors)
  │  │  │
  │  │  └─ NO → Keep late fusion, improve single-modality
  │  │
  │  └─ NO → Focus on better per-modality embeddings
  │           Try harmonization (ComBat, MURD)
```

---

## 📊 Data Status

!!! warning "Note: Data Documentation vs Availability"
    This KB documents **how to use data**, not **when data is ready**.  
    Actual data availability is project-specific and tracked elsewhere.

| Dataset | Docs | Data Status | Notes |
|---------|:----:|:-----------:|-------|
| **hg38 reference** | ✅ | ✅ Available | Public reference genome |
| **Genomic benchmarks** | ✅ | ✅ Available | Public benchmarks |
| **UKB fMRI/sMRI** | ✅ | 🟡 Pending | Features can be downloaded (check with 정우/상윤 선생님) |
| **Genetics embeddings** | ✅ | 🟡 Pending | From Prof. Joo (offline, pre-trained) |
| **Cha Hospital dev cohort** | ✅ | 🟡 Future | For developmental research |

---

## 🛠️ Utilities

```bash
# Validate all YAML cards
python scripts/manage_kb.py validate models
python scripts/manage_kb.py validate datasets

# Query embedding recipe
python scripts/manage_kb.py ops strategy genetics_joo_mdd_cog_v1

# Query harmonization method
python scripts/manage_kb.py ops harmonization combat_smri

# View docs locally
mkdocs serve  # Visit http://localhost:8000

# Online docs
https://allison-eunse.github.io/neuro-omics-kb/
```

---

## ❓ FAQ

!!! question "Which genetics FM should I use?"
    **Answer:** Start with Prof. Joo's pipeline (`genetics_joo_mdd_cog_v1`):
    
    - 38 MDD genes from Yoon et al.
    - RC-averaged embeddings
    - Already validated in their work
    
    Then compare with other FMs if needed (Caduceus, DNABERT-2, Evo2)

!!! question "Should I use sMRI or fMRI features?"
    **Answer:** Both are documented:
    
    - **sMRI:** FreeSurfer ROIs (~176 features) → Good for structural analysis
    - **fMRI:** Parcellation data available → Ask 정우/상윤 선생님 for fMRI-gene analysis guidance
    
    Start with whichever is easier to download first.

!!! question "Do I need to build a new FM?"
    **No!** Stage-1 uses:
    
    - **Existing genetics FMs** (already trained by Prof. Joo)
    - **Existing brain FMs** (SwiFT, BrainLM, etc.)
    - **Late fusion** = just concatenate embeddings
    
    Only escalate to two-tower/unified FM if Stage-1 shows clear fusion benefit.

!!! question "What about Cha Hospital / developmental data?"
    **Future work.** The KB has:
    
    - Dataset card template: `kb/datasets/cha_dev_longitudinal.yaml`
    - Embedding recipes: `cha_dev_smri_pca64_v1`, `cha_dev_eeg_fm_v1`, `cha_dev_behaviour_latent_v1`
    - Experiment templates: `configs/experiments/dev_01_brain_only_baseline.yaml`
    
    **Focus on UKB first** (Jan-Feb wrap-up), then extend to developmental.

---

## 🎯 Key Principle

**This KB answers:**
- ✅ "How do I extract embeddings?"
- ✅ "Which FM should I use?"
- ✅ "How do I run CCA?"
- ✅ "When should I escalate to two-tower?"

**Not:**
- ❌ "Is UKB data ready yet?" (operational, not documentation)
- ❌ "Should I commit this result?" (project management, not KB)

---

## 📞 Questions?

- **Model choice:** Check `docs/models/<category>/index.md`
- **Integration strategy:** Read `docs/integration/integration_strategy.md`
- **Embedding recipes:** Query `python scripts/manage_kb.py ops strategy <id>`
- **Everything else:** Ask Allison or check online docs

---

**Bottom Line:** This repo is your **map + spec**. Run Stage-1 experiments (CCA + prediction baselines) end-to-end, then decide on escalation based on results.

**Jan-Feb Goal:** Complete Stage-1 with offline genetics embeddings + brain features → document results → decide next steps.

