# 🏥 Multimodal & Clinical Foundation Models

> **Unified multimodal architectures informing gene-brain-behavior integration**

---

## 📋 Overview

This section covers multimodal and clinical foundation models that integrate multiple modalities beyond genetics and neuroimaging, including medical imaging, text, video, and clinical data. These models represent the state-of-the-art in unified multimodal AI for healthcare and general-purpose vision-language understanding.

## 🎯 Models in this Section

### General Multimodal Models

| Model | Architecture | Key Innovation | Parameters | Documentation |
|:------|:-------------|:---------------|:-----------|:--------------|
| <span class="multimodal">**[Flamingo](flamingo.md)**</span> | Perceiver + gated cross-attention | Few-shot multimodal VLM via frozen encoders | 3B / 4B / 9B / 80B | [Code Walkthrough](../../code_walkthroughs/flamingo_walkthrough.md) |
| <span class="multimodal">**[BAGEL](bagel.md)**</span> | MoT decoder + SigLIP + VAE | Unified understanding + generation | 7B active / 14B total | [Code Walkthrough](../../code_walkthroughs/bagel_walkthrough.md) |
| <span class="multimodal">**[MoT](mot.md)**</span> | Sparse transformer | Modality-aware FFNs (~55% FLOPs) | Scales to 7B+ | [Code Walkthrough](../../code_walkthroughs/mot_walkthrough.md) |

### Medical Multimodal Models

| Model | Architecture | Clinical Focus | Languages | Documentation |
|:------|:-------------|:---------------|:----------|:--------------|
| <span class="multimodal">**[M3FM](m3fm.md)**</span> | CLIP + medical LLM | CXR + CT report generation | EN + CN | [Code Walkthrough](../../code_walkthroughs/m3fm_walkthrough.md) |
| <span class="multimodal">**[Me-LLaMA](me_llama.md)**</span> | Continual pretrained LLaMA | Medical knowledge integration | English | [Code Walkthrough](../../code_walkthroughs/melamma_walkthrough.md) |
| <span class="multimodal">**[TITAN](titan.md)**</span> | Vision transformer | Whole-slide pathology (gigapixel) | English | [Code Walkthrough](../../code_walkthroughs/titan_walkthrough.md) |

### Medical Data Catalog

| Resource | Coverage | Use Case | Documentation |
|:---------|:---------|:---------|:--------------|
| <span class="reference">**[FMS-Medical](fms_medical.md)**</span> | 100+ medical datasets | Dataset discovery + benchmarking | [Code Walkthrough](../../code_walkthroughs/fms_medical_walkthrough.md) |

---

## Why Multimodal Models Matter for Neuro-Omics

While the Neuro-Omics KB focuses primarily on **genetics** and **brain** foundation models, understanding multimodal integration patterns is critical for:

1. **Integration Strategy Design**
   - BAGEL and MoT demonstrate successful architectures for combining diverse modalities
   - Medical models show how to handle domain-specific data with limited labels
   
2. **Zero-Shot Transfer Learning**
   - Medical models excel at cross-domain and cross-language generalization
   - These patterns inform how to transfer gene-brain models to new cohorts
   
3. **Clinical Translation**
   - Medical VLMs provide templates for integrating brain imaging with clinical text
   - Pathology models show how to scale vision transformers to gigapixel inputs
   
4. **LLM Integration**
   - Me-LLaMA demonstrates medical knowledge injection into general LLMs
   - This approach extends to neuro-omics applications (e.g., genetics literature + brain phenotypes)

---

## Integration with ARPA-H Brain-Omics Model (BOM)

The BOM vision includes multimodal integration beyond gene-brain fusion:

```
Gene embeddings → |
                  | → Brain-Omics Model (BOM) → Clinical predictions
Brain embeddings →|                             ↓
                  |                         Multimodal LLM
Clinical text    →|                         (reasoning + reports)
```

Multimodal models inform the BOM design in three ways:

### 1. Architecture Patterns

- **BAGEL/MoT:** Show how to build unified models with understanding + generation
- **M3FM:** Demonstrates two-tower CLIP-style alignment for medical domains
- **TITAN:** Provides hierarchical vision transformer patterns for multi-scale data

### 2. Training Strategies

- **Zero-shot capabilities:** Critical for rare diseases and new cohorts
- **Multilingual support:** Extends models to diverse global populations
- **Continual pretraining:** Me-LLaMA shows how to inject domain knowledge post-hoc

### 3. Clinical Workflows

- **Report generation:** Automated clinical summaries from multimodal inputs
- **Diagnosis support:** Combining embeddings for downstream classification
- **Few-shot adaptation:** Rapid deployment with minimal labeled data

---

## Model Selection Guide

Choose multimodal models based on your integration goals:

### For Architecture Design

- **If building unified understanding + generation:**
  - Start with **BAGEL** or **MoT** architectures
  - These show how to handle multiple modalities in one model

### For Medical Applications

- **If working with medical imaging + text:**
  - Use **M3FM** for CLIP-style alignment
  - Consider **TITAN** for pathology/high-resolution imaging

- **If integrating medical knowledge with LLMs:**
  - Study **Me-LLaMA** for continual pretraining approaches
  - See **FMS-Medical** for dataset selection

### For Zero-Shot Transfer

- **If targeting low-resource settings:**
  - All medical models demonstrate strong zero-shot capabilities
  - M3FM is particularly strong for cross-language transfer

---

## Next Steps

1. **Read model pages:**
   - Each model page includes architecture details, integration strategies, and reference materials
   
2. **Review integration patterns:**
   - See [Design Patterns](../../integration/design_patterns.md) for fusion architectures
   - Check [Multimodal Architectures](../../integration/multimodal_architectures.md) for detailed integration guides

3. **Explore code walkthroughs:**
   - Practical implementation details in [Code Walkthroughs](../../code_walkthroughs/index.md)

4. **Study paper summaries:**
   - Full paper notes available in Research Papers section (see site navigation)

---

## Reference Materials

- **Integration strategy:** [integration/integration_strategy.md](../../integration/integration_strategy.md)
- **Design patterns:** [integration/design_patterns.md](../../integration/design_patterns.md)
- **Multimodal architectures:** [integration/multimodal_architectures.md](../../integration/multimodal_architectures.md)
- **ARPA-H vision:** See integration plan (Nov 2025) in decisions folder


