# Missing Paper Cards Analysis

## Summary

**Model Cards**: 15 total (excluding template)
**Paper Cards**: 14 total (excluding template)
**Mismatch**: 3 models have paper markdown summaries but **NO paper YAML cards**

---

## Missing Paper YAML Cards

### 1. **M3FM** ❌
- **Model Card**: ✅ `kb/model_cards/m3fm.yaml`
- **Paper Markdown**: ✅ `docs/generated/kb_curated/papers-md/m3fm_2025.md`
- **Paper YAML Card**: ❌ **MISSING**
- **Paper Info**:
  - Title: "M3FM: A Multimodal, Multidomain, Multilingual Medical Foundation Model for Zero‑Shot Clinical Diagnosis"
  - Authors: Fenglin Liu, Zheng Li, Qingyu Yin, et al.
  - Year: 2025
  - Venue: npj Digital Medicine
  - DOI: 10.1038/s41746-024-01339-7
- **Why Missing**: Paper markdown exists but YAML card was never created

### 2. **TITAN** ❌
- **Model Card**: ✅ `kb/model_cards/titan.yaml`
- **Paper Markdown**: ✅ `docs/generated/kb_curated/papers-md/titan_2025.md`
- **Paper YAML Card**: ❌ **MISSING**
- **Paper Info**:
  - Title: "TITAN: A Multimodal Whole-Slide Foundation Model for Computational Pathology"
  - Authors: Tong Ding, Sophia J. Wagner, Andrew H. Song, et al.
  - Year: 2025
  - Venue: Nature Medicine
- **Why Missing**: Paper markdown exists but YAML card was never created

### 3. **Me-LLaMA** ❌
- **Model Card**: ✅ `kb/model_cards/me_llama.yaml`
- **Paper Markdown**: ✅ `docs/generated/kb_curated/papers-md/me_llama_2024.md`
- **Paper YAML Card**: ❌ **MISSING**
- **Paper Info**:
  - Title: "Me-LLaMA: Medical Foundation Large Language Models for Comprehensive Text Analysis and Clinical Reasoning"
  - Authors: Qianqian Xie, Qingyu Chen, Aokun Chen, et al.
  - Year: 2024
  - Venue: Preprint (medical AI / biomedical informatics)
- **Why Missing**: Paper markdown exists but YAML card was never created

---

## Models Without Papers (Expected)

### 4. **DNABERT-2** ⚠️
- **Model Card**: ✅ `kb/model_cards/dnabert2.yaml`
- **Paper Markdown**: ❌ No markdown summary
- **Paper YAML Card**: ❌ No YAML card
- **Status**: May not have a published paper (or paper not yet curated)
- **Action**: Check if paper exists; if yes, create both markdown and YAML card

### 5. **SwiFT** ⚠️
- **Model Card**: ✅ `kb/model_cards/swift.yaml`
- **Paper Markdown**: ❌ No markdown summary
- **Paper YAML Card**: ❌ No YAML card
- **Status**: May not have a published paper (or paper not yet curated)
- **Action**: Check if paper exists; if yes, create both markdown and YAML card

---

## Models That Are Not Real Papers (Conceptual/Placeholder)

### 6. **llm_semantic_bridge**
- **Model Card**: ✅ `kb/model_cards/llm_semantic_bridge.yaml`
- **Status**: Conceptual model for ARPA-H BOM, not a published paper
- **Action**: No paper card needed

### 7. **vlm_dev_clinical**
- **Model Card**: ✅ `kb/model_cards/vlm_dev_clinical.yaml`
- **Status**: Conceptual model for developmental clinical VLM, not a published paper
- **Action**: No paper card needed

### 8. **tabpfn**
- **Model Card**: ✅ `kb/model_cards/tabpfn.yaml`
- **Status**: Different domain (tabular data), may not be relevant for neuro-omics
- **Action**: Verify if paper card needed

---

## Paper Cards That Are Not Models

These are integration/method papers, not model papers:

- `ensemble_integration_li2022.yaml` - Integration method paper
- `oncology_multimodal_waqas2024.yaml` - Integration method paper
- `yoon_biokdd2025.yaml` - Integration method paper
- `gwas_diverse_populations.yaml` - Population genetics paper
- `prs_guide.yaml` - Population genetics guide

**These are correct** - they document methods/strategies, not specific models.

---

## Action Items

### High Priority (Create Paper YAML Cards)

1. **Create `kb/paper_cards/m3fm_2025.yaml`**
   - Use `m3fm_2025.md` as source
   - Follow `bagel_2025.yaml` as template
   - Link to model card: `kb/model_cards/m3fm.yaml`

2. **Create `kb/paper_cards/titan_2025.yaml`**
   - Use `titan_2025.md` as source
   - Follow `bagel_2025.yaml` as template
   - Link to model card: `kb/model_cards/titan.yaml`

3. **Create `kb/paper_cards/me_llama_2024.yaml`**
   - Use `me_llama_2024.md` as source
   - Follow `bagel_2025.yaml` as template
   - Link to model card: `kb/model_cards/me_llama.yaml`

### Medium Priority (COMPLETED ✅)

4. **DNABERT-2** ✅
   - **Paper found**: "DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genomes" (ICLR 2024)
   - **Created**: `kb/paper_cards/dnabert2_2024.yaml`
   - **Authors**: Zhihan Zhou et al.
   - **Link**: [arXiv:2306.15006](https://arxiv.org/abs/2306.15006)

5. **SwiFT** ✅
   - **Paper found**: "SwiFT: Swin 4D fMRI Transformer" (NeurIPS 2023)
   - **Created**: `kb/paper_cards/swift_2023.yaml`
   - **Authors**: Peter Yongho Kim et al.
   - **Link**: [arXiv:2307.05916](https://arxiv.org/abs/2307.05916)

### Low Priority (COMPLETED ✅)

6. **TabPFN** ✅
   - **Paper found**: "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second" (Nature 2024)
   - **Created**: `kb/paper_cards/tabpfn_2024.yaml`
   - **Authors**: Noah Hollmann et al.
   - **Link**: [Nature](https://www.nature.com/articles/s41586-024-08328-6)
   - **Relevance**: Used as baseline predictor for tabular fusion tasks (late fusion with LR/GBDT)

---

## Expected Count After Fixes

**Model Cards**: 15 (unchanged)
**Paper Cards**: 20 (14 original + 6 new)
- 6 new: m3fm_2025, titan_2025, me_llama_2024, dnabert2_2024, swift_2023, tabpfn_2024

**Note**: The count won't match exactly because:
- Some paper cards document integration methods (not models): ensemble_integration_li2022, oncology_multimodal_waqas2024, yoon_biokdd2025, mmfm_2025, etc.
- Some model cards are conceptual (no papers): llm_semantic_bridge, vlm_dev_clinical
- TabPFN is included as a relevant baseline predictor for tabular fusion tasks

---

## Template Reference

Use `kb/paper_cards/template.yaml` or `kb/paper_cards/bagel_2025.yaml` as reference for creating new paper cards.

