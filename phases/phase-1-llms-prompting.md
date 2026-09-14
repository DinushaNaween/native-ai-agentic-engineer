# Phase 1 — LLMs & Prompt Engineering
**Duration**: Weeks 5–8 (Oct 12 – Nov 8, 2026)  
**Status**: 🔲 Not Started

> Learn to talk to models effectively and understand their internals.

---

## 🎯 Learning Topics

### 1. LLM Landscape
- GPT-4o (OpenAI) — capabilities, pricing, API
- Claude 3.5 Sonnet (Anthropic) — strengths, constitutional AI
- Gemini (Google) — multimodal features
- Llama 3.x (Meta) — open-source, self-hosted
- Mistral — efficient open models
- When to use which model

### 2. Prompt Engineering Patterns
- Zero-shot prompting
- Few-shot prompting (examples in prompt)
- Chain-of-Thought (CoT) — "Let's think step by step"
- Tree-of-Thought (ToT) — branching reasoning
- ReAct pattern (Reasoning + Acting)
- System prompts vs user prompts
- Role-playing / persona prompts
- Negative prompting

### 3. Structured Outputs
- JSON mode
- Function calling / tool use
- Pydantic + LLMs for structured extraction
- Instructor library

### 4. Context Window Management
- What tokens are and how to count them
- Context window limits by model
- Chunking long documents
- Sliding window approach
- Summarization chains

### 5. Fine-tuning Basics
- When to fine-tune vs prompt engineer
- LoRA (Low-Rank Adaptation)
- QLoRA (Quantized LoRA)
- PEFT — Parameter Efficient Fine-Tuning
- Datasets for fine-tuning
- Using Hugging Face for fine-tuning

### 6. LLM APIs
- OpenAI Python SDK
- Anthropic Python SDK
- Google Gemini SDK
- Hugging Face Inference API
- Managing API keys securely

### 7. LLM Evaluation
- BLEU and ROUGE scores (limitations)
- LLM-as-a-judge
- Human evaluation frameworks
- Benchmark datasets (MMLU, HumanEval, etc.)

---

## 📚 Learning Resources

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| DeepLearning.AI: ChatGPT Prompt Engineering | Course (Free) | ⭐⭐⭐ | https://deeplearning.ai/short-courses |
| Anthropic Prompt Library | Docs | ⭐⭐⭐ | https://docs.anthropic.com/en/prompt-library |
| OpenAI Cookbook | Code Examples | ⭐⭐⭐ | https://cookbook.openai.com |
| Prompt Engineering Guide | Reference | ⭐⭐⭐ | https://promptingguide.ai |
| Lilian Weng's Blog | Blog | ⭐⭐ | https://lilianweng.github.io |
| Hugging Face NLP Course | Course (Free) | ⭐⭐ | https://huggingface.co/learn/nlp-course |
| Instructor Library Docs | Docs | ⭐⭐ | https://python.useinstructor.com |

---

## 🏗️ Hands-On Exercises

- [ ] Call OpenAI, Anthropic, and Gemini APIs from Python
- [ ] Build a structured data extractor using function calling
- [ ] Create a prompt library for a domain of your choice
- [ ] Implement a chain-of-thought prompt for a reasoning task
- [ ] Fine-tune a small model on a custom dataset (using Hugging Face)

---

## 🏗️ Phase Project: LLM Comparison Dashboard

Build a simple tool that:
1. Takes a prompt
2. Sends it to GPT-4o, Claude, and Gemini simultaneously
3. Displays responses side by side with latency and cost
4. Saves results for analysis

**Location**: `projects/phase-1-llm-comparison/` _(optional extra project)_

---

## ✅ Milestone Checkpoints

- [ ] Built a structured data extractor using function calling
- [ ] Compared 3 LLMs (GPT-4o, Claude, Gemini) on same task, documented results
- [ ] Created a reusable prompt library with 10+ prompts
- [ ] Understand the difference between system, user, and assistant roles

---

## 📝 LinkedIn Articles (This Phase)

### Article 3: "Prompt Engineering is a Real Skill — Here's Why"
**Draft**: `notes/articles/article-03-prompt-engineering.md`  
**Post When**: Week 6

### Article 4: "I Compared GPT-4o vs Claude vs Gemini"
**Draft**: `notes/articles/article-04-llm-comparison.md`  
**Post When**: End of Week 8

### Article 5: "Function Calling: The Feature That Makes LLMs Actually Useful"
**Draft**: `notes/articles/article-05-function-calling.md`  
**Post When**: Week 7

---

## 🔗 Key Papers

- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)
- [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685)
