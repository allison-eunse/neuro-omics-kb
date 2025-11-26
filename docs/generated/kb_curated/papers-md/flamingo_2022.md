---
title: "Flamingo: a Visual Language Model for Few-Shot Learning"
authors: "Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan"
year: 2022
venue: "NeurIPS 2022"
---

# Flamingo: a Visual Language Model for Few-Shot Learning

**Authors:** Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, et al. (DeepMind)  
**Year:** 2022  
**Venue:** NeurIPS 2022

---

## 1. Classification

- **Domain Category:**  
  - Vision / VLM / Multimodal FM  
  - Flamingo is a visual language model (VLM) that integrates vision and language for few-shot learning on image and video understanding tasks.

- **FM Usage Type:**  
  - Core FM development **+** Multimodal FM or cross-modal integration

- **Key Modalities:**  
  - Images (high-resolution from web data)
  - Videos (short clips, average 22 seconds)
  - Text (interleaved captions, questions, answers)

---

## 2. Executive Summary

Flamingo is a family of Visual Language Models (VLMs) that achieve state-of-the-art few-shot learning on image and video understanding tasks by being prompted with a few input/output examples—analogous to GPT-3's few-shot text learning. The model bridges pretrained vision and language models through novel architectural components: a **Perceiver Resampler** that converts variable-size visual features into fixed visual tokens, and **GATED XATTN-DENSE layers** that condition frozen language models on visual representations via gated cross-attention. Flamingo handles arbitrarily interleaved sequences of images/videos and text, enabling natural few-shot prompting. Trained on billions of web-scraped multimodal examples (interleaved image-text from webpages, image-text pairs, video-text pairs) without task-specific annotations, a single Flamingo model achieves new state-of-the-art few-shot performance on 16 diverse benchmarks and outperforms fine-tuned models on 6 tasks despite using only 32 examples (1000× less data). The largest model (Flamingo-80B) sets new records on VQA and captioning tasks.

---

## 3. Problem Setup and Motivation

- **Scientific / practical problem:**  
  - Current vision-language models require extensive task-specific fine-tuning with thousands of annotated examples.
  - Contrastive models (CLIP) enable zero-shot classification but lack generative capabilities for open-ended tasks like captioning and VQA.
  - Goal: Build a model that rapidly adapts to new vision-language tasks using only a few examples, similar to GPT-3's few-shot learning for text.

- **Why this is hard:**  
  - **Bridging vision and language:** Vision encoders and language models are trained separately; connecting them effectively while preserving both pretrained knowledges is non-trivial.
  - **Handling interleaved multimodal sequences:** Few-shot learning requires processing sequences like (image₁, text₁), (image₂, text₂), ..., (query_image, ?).
  - **Variable-size visual inputs:** Images and videos have variable resolutions; language models expect fixed-size token sequences.
  - **Large-scale training data:** Few-shot learning requires massive pretraining on diverse multimodal data (billions of examples).
  - **Training stability:** Combining frozen pretrained models with new trainable components requires careful initialization and gating mechanisms.

---

## 4. Data and Modalities

- **Pretraining data:**  
  - **M3W (MultiModal MassiveWeb):** ~43M webpages with interleaved images and text (up to 5 images per sequence, 256 tokens).
  - **ALIGN:** 1.8B image-text pairs with alt-text descriptions.
  - **LTIP (Long Text & Image Pairs):** 312M image-text pairs with longer, higher-quality descriptions.
  - **VTP (Video & Text Pairs):** 27M short videos (average 22 seconds) with sentence descriptions.

- **Modalities:**  
  - **Images:** High-resolution images from webpages and image-text pairs.
  - **Videos:** Short video clips (1 FPS sampling) with temporal embeddings.
  - **Text:** Captions, questions, answers, descriptions, interleaved with visual content.

- **Preprocessing / representation:**  
  - **Vision encoder:** Pretrained NFNet-F6 (NormalizerFree ResNet) with contrastive pretraining; outputs 2D spatial grid flattened to 1D sequence.
  - **Perceiver Resampler:** Converts variable number of visual features to fixed 64 visual tokens using learned latent queries.
  - **Text:** Tokenized using language model's tokenizer; special tokens `<image>`, `<EOC>` (end of chunk).

---

## 5. Model / Foundation Model

- **Model Type:**  
  - Multimodal autoregressive language model that generates text conditioned on interleaved visual and textual inputs.

- **Is it a new FM or an existing one?**  
  - **New FM.** Flamingo introduces a new family of VLMs with specific architectural innovations for few-shot learning.

- **Key components and innovations:**

  | Aspect                    | Details |
  |---------------------------|---------|
  | Vision encoder            | Pretrained NFNet-F6 (frozen) with contrastive pretraining |
  | Perceiver Resampler       | Converts variable visual features → fixed 64 visual tokens via learned queries |
  | Language model            | Chinchilla LM (1.4B, 7B, 70B) - frozen |
  | GATED XATTN-DENSE layers  | Interleaved between LM layers: gated cross-attention + gated FF, initialized at 0 |
  | Image-causal masking      | Text tokens attend only to immediately preceding image, not all previous images |
  | Model sizes               | Flamingo-3B, 9B, 80B (based on Chinchilla 1.4B, 7B, 70B) |

- **Training setup (high level):**
  - **Objective:** Autoregressive text generation conditioned on interleaved visual inputs.
  - **Loss:** Weighted sum of per-dataset negative log-likelihoods.
  - **Training strategy:** Gradient accumulation over all datasets (outperforms round-robin).
  - **Few-shot adaptation:** No fine-tuning; simply prompt with (image, text) example pairs followed by query.

---

## 6. Multimodal / Integration Aspects (If Applicable)

- **Modalities integrated:**  
  - Vision (images/videos) and text through late fusion with cross-attention.

- **How integration works:**  
  - Vision and language processed separately (frozen encoders), then fused via **GATED XATTN-DENSE layers**.
  - **Perceiver Resampler** bridges vision encoder and language model by converting visual features to tokens.
  - **Interleaved sequences:** Support arbitrary mixing of visual and textual inputs through image-causal masking.

- **Why this integration is useful / new capabilities:**  
  - **Few-shot learning:** Model adapts to new tasks by seeing a few (image, text) examples.
  - **Open-ended generation:** Can generate captions, answers, descriptions conditioned on images/videos.
  - **Multi-image reasoning:** Processes sequences of multiple images with interleaved text (e.g., visual dialogue).
  - **Zero-shot capabilities:** Works out-of-the-box on tasks not seen during training.

---

## 7. Experiments and Results

- **Benchmarks:**  
  - 16 diverse tasks: VQAv2, OK-VQA, COCO captioning, TextVQA, VizWiz, MSRVTTQA, VATEX, VisDial, HatefulMemes, etc.

- **Baselines:**  
  - Fine-tuned task-specific models, CLIP, other VLMs.

- **Key findings (trends):**  
  - **State-of-the-art few-shot performance:** Flamingo-80B sets new SotA on 9 of 16 tasks with 4-32 shots.
  - **Outperforms fine-tuned models on 6 tasks** despite using only 32 examples (vs. thousands for fine-tuning).
  - **Performance by task:**
    - VQAv2: 57.8% (32-shot) vs. 80.2% (fine-tuned SotA)
    - COCO captioning: 113.8 CIDEr (32-shot) vs. 143.3 (fine-tuned)
    - Strong video understanding on MSRVTTQA, VATEX, NextQA
  - **Scaling:** Performance improves with model size (3B → 9B → 80B) and number of shots (0 → 4 → 32).

- **Ablations:**
  - **Perceiver Resampler** outperforms plain Transformer and MLP alternatives.
  - **Gating mechanism** (tanh initialization) improves training stability and performance.
  - **Image-causal masking** (attend only to immediately preceding image) outperforms attending to all previous images.
  - **Dataset weighting** is crucial; gradient accumulation outperforms round-robin sampling.

---

## 8. Strengths, Limitations, and Open Questions

**Strengths:**

- **Powerful few-shot learning:** Achieves SotA on many tasks with just 4-32 examples, dramatically reducing annotation requirements.
- **Open-ended generation:** Can generate free-form text (captions, answers) unlike contrastive models (CLIP).
- **Handles diverse tasks:** Single model works on classification, captioning, VQA, dialogue, video understanding.
- **Leverages pretrained models:** Effectively combines frozen vision and language models, preserving their knowledge.
- **Scalable architecture:** Works across model sizes (3B to 80B) with consistent improvements.

**Limitations:**

- **Still behind fine-tuned models:** On some tasks, fine-tuned models with thousands of examples outperform Flamingo's few-shot performance.
- **Compute intensive:** Training on billions of examples and 80B parameters requires massive compute resources.
- **Limited to vision-language:** Doesn't handle other modalities (audio, 3D, biological data).
- **Frozen encoders:** Cannot adapt vision or language encoders to new domains without retraining.

**Open questions and future directions:**

1. How can few-shot performance be further improved to match or exceed fine-tuned models across all tasks?
2. Can similar architectures be extended to other modalities (audio, 3D scenes, biological data)?
3. How to make training more compute-efficient while maintaining few-shot capabilities?
4. Can the gated cross-attention mechanism be adapted to biological multimodal settings (gene-brain-behavior)?

---

## 9. Context and Broader Impact

- **Position in the landscape:**  
  - Flamingo demonstrates that large-scale web data training enables powerful in-context learning capabilities (previously seen only in text-only LLMs) for multimodal tasks.
  - Bridges the gap between contrastive models (CLIP) and generative models, offering both zero-shot and few-shot capabilities.

- **Relation to well-known ideas:**  
  - Extends **GPT-3's few-shot learning paradigm** to vision-language tasks.
  - Uses **Perceiver-style** cross-attention for vision-language bridging.
  - Combines ideas from **frozen encoders** (preserving pretrained knowledge) and **trainable connectors** (enabling multimodal fusion).

- **Why this paper is a useful reference:**  
  - **For multimodal FM research:** Provides a blueprint for bridging vision and language FMs with minimal trainable parameters.
  - **For gene-brain-behavior integration:** Architectural principles (Perceiver Resampler, gated cross-attention, interleaved sequences) could be adapted to biological multimodal settings.
  - **For few-shot learning:** Demonstrates the power of large-scale web data for enabling in-context learning.

---

## 10. Key Takeaways (Bullet Summary)

- **Problem:**  
  - Vision-language models require extensive fine-tuning; goal is to enable few-shot learning like GPT-3.

- **Method / model:**  
  - Flamingo is a family of VLMs (3B to 80B) that bridge frozen vision encoders and language models via **Perceiver Resampler** and **GATED XATTN-DENSE layers**.
  - Trained on billions of web-scraped multimodal examples (interleaved image-text, image-text pairs, video-text pairs).

- **Results:**  
  - State-of-the-art few-shot performance on 16 benchmarks; outperforms fine-tuned models on 6 tasks with only 32 examples.
  - Largest model (Flamingo-80B) sets new records on VQA and captioning.

- **Why it matters:**  
  - Shows that large-scale web data enables powerful in-context learning for multimodal tasks.
  - Demonstrates effective architectural patterns for bridging frozen pretrained models.
  - Provides a reference for adapting few-shot learning to biological multimodal settings (gene-brain-behavior).

---
