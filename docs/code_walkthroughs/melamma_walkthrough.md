# Me-LLaMA Code Walkthrough

> **KB references:** [Me-LLaMA paper note](../generated/kb_curated/papers-md/me_llama_2024.md)

## Overview
Me-LLaMA is a suite of open-source medical foundation models (13B/70B) developed through continual pre-training and instruction tuning of LLaMA2. It leverages a heterogeneous corpus of biomedical literature (PubMed), clinical notes (MIMIC-IV/MIMIC-CXR), and general domain data to balance domain specificity with general reasoning. The repository provides evaluation scripts, training recipes, and inference examples for both base and chat-aligned versions.^[```33:36:external_repos/me-lamma/README.md```]

## At-a-Glance
| Architecture | Params / Scale | Context | Inputs | Key capabilities | Repo |
| --- | --- | --- | --- | --- | --- |
| LLaMA-2 based (Continual Pre-training + LoRA Tuning) | 13B & 70B parameters | 129B tokens mixed corpus (15:1:4 biomedical:clinical:general) | Text (clinical notes, papers, guidelines) | Medical reasoning, instruction following, zero-shot evaluation on PubMedQA/MedQA. | [GitHub](https://github.com/BIDS-Xu-Lab/Me-LLaMA) / [PhysioNet](https://www.physionet.org/content/me-llama/1.0.0/) |

### Environment & Hardware Notes
- **Installation:** Requires `torch` and `transformers`. Evaluation dependencies managed via `poetry` in `src/medical-evaluation`.^[```144:152:external_repos/me-lamma/README.md```]
- **Compute:** Developed on A100 GPUs (160x for pre-training) and H100 GPUs (8x for tuning). Local inference runs on standard GPU setups via Hugging Face pipelines.^[```80:89:external_repos/me-lamma/README.md```]
- **Access:** Models require PhysioNet credentialed access; datasets available via Hugging Face collection.^[```41:44:external_repos/me-lamma/README.md```]

## Key Components

### Training Pipeline (`README.md`)
The training strategy emphasizes **continual pre-training** followed by **instruction tuning**:
1.  **Continual Pre-training:** 129B tokens mixed from PubMed (15), MIMIC (1), and RedPajama (4). Uses AdamW, cosine scheduler (0.05 warmup), and bf16 precision with DeepSpeed parallelism.
2.  **Instruction Tuning:** 214K samples trained for 3 epochs using LoRA parameter-efficient fine-tuning on H100s.
This approach mitigates catastrophic forgetting while injecting specialized medical knowledge.^[```64:91:external_repos/me-lamma/README.md```]

### Inference Stack (`README.md`)
Inference is standard Hugging Face `transformers`. The README provides snippets for both high-level `pipeline` usage and low-level `AutoModelForCausalLM` control:

**Basic Generation:**
```python
from transformers import pipeline
pipe = pipeline("text-generation", model="path/to/Me-LLaMA")
print(pipe("The medical condition is characterized by", num_return_sequences=1))
```

**Granular Control:**
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("path/to/Me-LLaMA")
model = AutoModelForCausalLM.from_pretrained("path/to/Me-LLaMA")
input_ids = tokenizer("[INPUT]", return_tensors="pt").input_ids
gen = model.generate(input_ids, max_length=50)
print(tokenizer.decode(gen[0]))
```
^[```93:138:external_repos/me-lamma/README.md```]

### Evaluation Harness (`src/medical-evaluation`)
The repository includes a robust evaluation suite using `poetry` and `src/eval.py`. It supports:
- **Hugging Face Models:** Evaluate local or Hub models (e.g., `hf-causal-vllm`) against medical benchmarks (PUBMEDQA, MedQA, BioNLI, etc.).
- **Commercial APIs:** Compare against GPT-4 by swapping the model argument.
- **Metrics:** Includes BARTScore integration (`src/metrics/BARTScore`).

**Run Example:**
```bash
poetry run python src/eval.py \
    --model "hf-causal-vllm" \
    --model_args "pretrained=meta-llama/Llama-2-7b-chat-hf" \
    --tasks "PUBMEDQA,MedQA,MedMCQA,..."
```
^[```139:190:external_repos/me-lamma/README.md```]

## Integration Hooks
- **Benchmark Alignment:** Use the task list in `scripts/run_evaluation.sh` ("PUBMEDQA,MedQA...") as a standard checklist for evaluating new KB models.
- **Dataset Collection:** The [Hugging Face collection](https://huggingface.co/collections/clinicalnlplab/ibe-65de0abfafad82f111fe5392) referenced is a valuable resource for populating `kb/datasets/`.
- **Baseline Comparisons:** Use the provided GPT-4 evaluation scripts to establish strong baselines for neuro-omics tasks.
