---
title: Multimodal FM Patterns — Integration Guidance Card
status: draft
updated: 2025-11-19
tags: [integration, multimodal, clinical, bom, patterns]
---

# Multimodal Foundation Model Patterns for Brain-Omics

**Source models:** BAGEL, MoT, M3FM, Me-LLaMA, TITAN, FMS-Medical Catalog  
**Type:** Cross-model integration pattern synthesis  
**Best for:** Choosing multimodal architectures and fusion strategies that align with the ARPA-H Brain-Omics Model (BOM) vision.

---

## Problem It Solves

**Challenge:** Given many powerful multimodal FMs (vision–language models, unified MoT transformers, medical LLMs), how do we:

- Decide **which architectural pattern** (two-tower CLIP, unified MoT, hierarchical ViT, LLM-as-bridge) to use for **gene–brain–behavior–text** integration?  
- Prioritize models and patterns that **match ARPA-H BOM goals**: zero-shot generalization, label efficiency, clinical interpretability, and scalability across sites and populations.  
- Avoid over-engineering (e.g., jumping to BAGEL-scale unified models) before late fusion and simpler patterns are exhausted.

**Solution (this card):** Compare and contrast multimodal FMs and papers to extract **three reusable integration patterns** that can be slotted into the Neuro-Omics KB and BOM roadmap:

1. **Two-Tower CLIP-Style Alignment** (M3FM, TITAN stage 2/3)  
2. **Unified MoT-Style Multimodal Transformer** (BAGEL + MoT)  
3. **LLM-as-Semantic Bridge** (Me-LLaMA + others)

Each pattern is summarized below with **strengths, benchmarks, and ARPA-H fit**, then mapped to a **recommended escalation path**.

---

## Core Multimodal Patterns

### Pattern 1 — Two-Tower CLIP-Style Alignment

**Representative models:**  
- M3FM (medical vision–language: CXR/CT + bilingual reports)  
- TITAN (histopathology slides + ROI captions + pathology reports)  

**Mechanism:**

```text
Image encoder (brain / CXR / WSI)  →  visual_embedding
Text encoder (medical LLM / encoder) → text_embedding
           ↓                                   ↓
         CLIP-style contrastive loss in shared latent space
           ↓
      Downstream heads (classification, retrieval, report generation)
```

**Key properties (from M3FM/TITAN):**
- **Label efficiency:** Strong zero-shot / few-shot transfer once alignment is learned.
- **Modality decoupling:** Vision and text encoders can be updated or swapped independently.
- **Multilingual extension:** Language side can be extended (e.g., English ↔ Korean) without retraining vision encoder.
- **Clinical relevance:** Direct path from images → clinically meaningful text outputs.

**When it shines (benchmarks & regimes):**
- Zero-shot report generation (M3FM) across CXR/CT and languages.  
- Cross-modal retrieval (TITAN) between slides and pathology reports.  
- Few-shot classification where **paired data** is available for pretraining.

---

### Pattern 2 — Unified MoT-Style Multimodal Transformer

**Representative models:**  
- BAGEL (unified text–image–video + generation)  
- MoT (modality-aware sparse transformers, Chameleon/Transfusion-style)

**Mechanism:**

```text
All modalities → token sequences → shared self-attention
                           ↓
         Modality-aware FFNs / experts (MoT-style)
                           ↓
                 Understanding + generation heads
```

**Key properties (from BAGEL/MoT):**
- **Unified reasoning:** All modalities interact through a single attention backbone.  
- **Modality-aware sparsity:** MoT decouples FFNs per modality → ~40–60% FLOP savings.  
- **Emergent capabilities:** BAGEL-style models show free-form visual manipulation, world modeling.  
- **Scalability:** Works at billion-parameter scales with careful engineering.

**When it shines:**
- Rich **cross-modal reasoning** tasks (e.g., world navigation, complex multimodal Q&A).  
- Scenarios where you want **joint understanding + generation** without bottlenecks.  
- High-resource settings where training unified models is computationally feasible.

---

### Pattern 3 — LLM-as-Semantic Bridge

**Representative models:**  
- Me-LLaMA (medical LLM with continual pretraining + instruction tuning)  
- Many general LLM + domain-adaptation pipelines

**Mechanism:**

```text
Modality encoders (genes, brain, behavior) → embeddings
                                     ↓
                       Projection into LLM token space
                                     ↓
                      Medical / neuro-omics LLM (Me-LLaMA-style)
                                     ↓
             Clinical reasoning, report generation, question answering
```

**Key properties (from Me-LLaMA + BOM vision):**
- **Domain-knowledge injection:** Continual pretraining on medical/neuroscience corpora.  
- **Instruction-tuned reasoning:** Multi-task prompts for QA, summarization, diagnosis.  
- **Human interface:** Natural language explanations for complex multimodal predictions.  

**When it shines:**
- Clinical reasoning and explanation tasks (e.g., “Why is this gene-brain pattern risky?”).  
- **Report generation** that must mix imaging, genetics, and behavioral findings.  
- Scenarios where interpretability and human-AI collaboration are central.

---

## When to Use Each Pattern (BOM-Centric View)

### Quick Decision Table

| Scenario | Recommended Pattern | Rationale |
|---------|---------------------|-----------|
| Zero-shot imaging → report (brain + text) | **Two-Tower CLIP** | M3FM/TITAN show strong label-efficiency |
| Scaling to many modalities with moderate compute | **MoT-style unified** | Modality-aware sparsity balances cost/performance |
| Clinician-facing reasoning / explanations | **LLM-as-Bridge** | Me-LLaMA demonstrates strong clinical NLP |
| Early BOM phases, limited data | **Two-Tower + LLM Bridge** | Leverage pretrained encoders & LLMs; avoid full unification |
| Later BOM phases, large paired multimodal datasets | **MoT-style unified + LLM Bridge** | Joint reasoning + language outputs |

---

## When to Defer These Patterns

⚠️ **Defer heavy multimodal patterns when:**
- You **haven’t yet demonstrated** that fusion beats strong single-modality baselines (per EI card).  
- You **lack sufficient paired data** to learn robust alignments (especially for two-tower and unified MoT).  
- Your **primary goal is mechanistic interpretability**, not raw predictive power.  
- Compute constraints make unified models impractical.

⚠️ **Prefer simpler approaches first:**
- Start with **late fusion + Ensemble Integration** (see [EI card](ensemble_integration.md)).  
- Use **CCA + permutation** to test for cross-modal structure before complex fusion.  
- Only escalate when fusion gains are **statistically significant and stable**.

---

## Adoption in Our Neuro-Omics / ARPA-H BOM Pipeline

### Phase 1 — Late Fusion + Diagnostic Probes (Current)

- Use **Ensemble Integration (EI)** as in `ensemble_integration.md`.  
- Evaluate whether gene+brain fusion improves AUROC/AUPRC vs. best single modality.  
- Use **CCA + permutation** to detect cross-modal structure.

### Phase 2 — Two-Tower CLIP-Style Alignment (Near Term)

**Goal:** Learn a shared **brain ↔ text** space for clinical reporting.

- Vision side: SwiFT / BrainLM encoders for fMRI/sMRI.  
- Text side: Me-LLaMA-style medical LLM or encoder.  
- Training: Contrastive loss on paired brain scans + radiology/clinical notes (M3FM-style).  
- Outputs:  
  - Zero-shot brain → report generation.  
  - Cross-modal retrieval (find similar brains given text, or vice versa).

**Fit to ARPA-H BOM:**
- Directly supports **clinical translation**, **zero-shot deployment**, and **multilingual extensions**.

### Phase 3 — LLM-as-Bridge for Gene–Brain–Behavior

**Goal:** Use a Me-LLaMA-style LLM as the **semantic hub** for:

```text
Genetics embeddings  → |
                       | → LLM token space → clinical text
Brain embeddings      → |
Behavioral measures   → |
```

- Continually pretrain LLaMA on neuroscience + genetics + clinical neurology corpora.  
- Instruction-tune for gene–brain–behavior reasoning tasks.  
- Use projections from gene/brain spaces into LLM embedding space for joint reasoning.

### Phase 4 — Unified MoT-Style Multimodal Transformer (Longer Term)

**Goal:** BOM-scale unified model across genes, brain, behavior, and text.

- Treat all modalities as tokens in a shared transformer (BAGEL/MoT-style).  
- Use **modality-aware FFNs** (MoT) to control compute while preserving cross-modal attention.  
- Optionally couple with LLM-as-bridge for **natural language interfaces** and clinical reasoning.

**Prerequisites:**
- Large paired multimodal dataset (≥ 50k subjects with gene+brain+behavior+text).  
- Demonstrated gains from Phase 2 & 3 patterns.  
- Stable training infrastructure for 7B+ parameter models.

---

## Caveats and Best Practices

### ⚠️ Benchmark Mismatch

Multimodal papers often report **general benchmarks** (e.g., VQA, CXR report BLEU) that don’t map 1:1 to neuro-omics.

**Mitigation:**  
- Define BOM-specific benchmarks: gene–brain prediction, cognitive scores, clinical endpoints.  
- Use multimodal FMs **as pattern references**, not drop-in benchmarking baselines.

### ⚠️ Domain Gap

Most multimodal FMs are trained on **radiology, pathology, or web data**, not genetics/brain.

**Mitigation:**  
- Reuse **architectural patterns** (two-tower, MoT, LLM-bridge) with domain-specific encoders (Caduceus, BrainLM, etc.).  
- Avoid directly applying off-the-shelf weights to neuro-omics without adaptation.

### ⚠️ Compute Budget

Unified models (BAGEL/MoT scale) are expensive to train and serve.

**Mitigation:**  
- Start with **two-tower + LLM-bridge** using frozen encoders and adapters.  
- Use **MoT-style sparsity** if/when moving to unified architectures.

---

## Practical Implementation Guide (Pattern 1 Example: Two-Tower Brain ↔ Text)

### Step 1 — Choose Encoders

| Component | Choice | Rationale |
|----------|--------|-----------|
| Brain encoder | BrainLM or SwiFT | Strong fMRI/sMRI FMs in KB |
| Text encoder | Me-LLaMA or medical BERT | Medical domain coverage |
| Projection head | 2–3 layer MLP | Map to shared 256–512D space |

### Step 2 — Train Contrastive Alignment

```python
# Pseudo-code for InfoNCE over brain ↔ text pairs
for brain_batch, text_batch in loader:
    b_emb = brain_proj(brain_encoder(brain_batch))   # [B, d]
    t_emb = text_proj(text_encoder(text_batch))      # [B, d]

    b_emb = F.normalize(b_emb, dim=-1)
    t_emb = F.normalize(t_emb, dim=-1)

    logits = b_emb @ t_emb.T / tau   # cosine similarities
    labels = torch.arange(len(brain_batch), device=logits.device)
    loss = (F.cross_entropy(logits, labels) + F.cross_entropy(logits.T, labels)) / 2
```

### Step 3 — Downstream Tasks

- **Retrieval:** nearest-neighbor in shared space.  
- **Zero-shot classification:** prompt-based thresholds in text space.  
- **Report generation:** condition LLM on aligned text embeddings.

---

## Reference Materials

**Multimodal papers (summaries):**
- [BAGEL (2025)](../../generated/kb_curated/papers-md/bagel_2025.md) — Unified MoT multimodal FM  
- [MoT (2025)](../../generated/kb_curated/papers-md/mot_2025.md) — Modality-aware sparse transformer  
- [M3FM (2025)](../../generated/kb_curated/papers-md/m3fm_2025.md) — Medical vision–language with two-tower CLIP  
- [Me-LLaMA (2024)](../../generated/kb_curated/papers-md/me_llama_2024.md) — Medical LLM via continual pretraining  
- [TITAN (2025)](../../generated/kb_curated/papers-md/titan_2025.md) — Multi-scale pathology VLM  
- [Multimodal FMs Survey (2025)](../../generated/kb_curated/papers-md/mmfm_2025.md) — Broader architectural landscape

**Model documentation:**
- [Multimodal Models](../multimodal/index.md) — Model-level documentation  
- [M3FM model card](https://github.com/allison-eunse/neuro-omics-kb/blob/main/kb/model_cards/m3fm.yaml)  
- [Me-LLaMA model card](https://github.com/allison-eunse/neuro-omics-kb/blob/main/kb/model_cards/me_llama.yaml)  
- [TITAN model card](https://github.com/allison-eunse/neuro-omics-kb/blob/main/kb/model_cards/titan.yaml)

**Integration guidance:**
- [Integration Strategy](../../integration/integration_strategy.md) — Overall fusion approach  
- [Design Patterns](../../integration/design_patterns.md) — Escalation from late fusion → MoT  
- [Multimodal Architecture Patterns](../../integration/multimodal_architectures.md) — Detailed pattern catalog  
- [Ensemble Integration (EI)](ensemble_integration.md) — Late fusion baseline  
- [Oncology Multimodal Principles](oncology_multimodal_review.md) — Fusion cautions & taxonomy

---

## Next Steps in Our Pipeline

1. **Catalog BOM requirements** against these three patterns (two-tower, MoT, LLM-bridge).  
2. **Prototype two-tower brain ↔ text alignment** using BrainLM/SwiFT + Me-LLaMA on UKB radiology data.  
3. **Design neuro-omics LLM continual pretraining corpus** (neuroscience + genetics + neurology).  
4. **Define data requirements** for potential MoT-style unified BOM (subject counts, modalities, sites).  
5. **Update ARPA-H BOM roadmap** with concrete pattern selection per phase.

---

## Key Takeaways

1. **Two-tower CLIP-style alignment** is the most immediately practical pattern for BOM: label-efficient, modular, clinically relevant.  
2. **MoT-style unified transformers** are powerful but should be a **Phase 3–4** goal once simpler fusion clearly helps and data is sufficient.  
3. **LLM-as-bridge** is essential for clinical impact: it turns multimodal embeddings into reasoning and explanations.  
4. Multimodal FM papers are best treated as **pattern libraries**, not plug-and-play models for neuro-omics.  
5. ARPA-H BOM should escalate from late fusion → two-tower + LLM-bridge → MoT-style unification, always gated by **evidence of fusion gains and data readiness**.

**Bottom line:** Use multimodal FMs to choose **integration patterns**, not just models—starting with two-tower and LLM-bridge patterns that best match ARPA-H’s emphasis on label-efficient, interpretable, clinically grounded brain-omics integration.


