# Phase 5 — Production AI Systems
**Duration**: Weeks 25–28 (Mar 1 – Mar 28, 2027)  
**Status**: 🔲 Not Started

> Ship AI systems that are reliable, scalable, observable, and cost-efficient.

---

## 🎯 Learning Topics

### 1. LLMOps vs MLOps
- What's different about LLM deployments
- Prompt versioning (not model versioning)
- Evaluation pipelines for production
- A/B testing prompts
- Cost monitoring and alerting
- LLMOps maturity model

### 2. Serving Infrastructure

#### FastAPI for AI
- Building LLM-powered REST APIs
- Async endpoints for streaming responses
- Background tasks for long-running agents
- Authentication & rate limiting

#### vLLM
- High-throughput LLM serving
- PagedAttention — why it's faster
- Continuous batching
- OpenAI-compatible API

#### Text Generation Inference (TGI)
- Hugging Face's serving solution
- Tensor parallelism for large models
- Token streaming

### 3. Observability & Tracing

#### LangSmith
- Trace every LLM call and agent step
- Datasets and evaluations
- Annotation queues for human review
- Monitoring dashboards

#### Arize Phoenix
- Open-source ML observability
- Span-based tracing
- Drift detection
- Query analysis

#### Weights & Biases
- Experiment tracking
- Prompt management
- Model monitoring

### 4. Cost Optimization

#### Semantic Caching
- Cache responses based on semantic similarity
- GPTCache library
- Redis + embedding similarity cache
- Expected savings: 40–70% on repeated queries

#### Smart Model Routing
- Route simple queries to cheaper models (GPT-4o-mini, Haiku)
- Route complex queries to powerful models (GPT-4o, Sonnet)
- Cascade routing — try cheap first, escalate if needed

#### Batching
- Batch multiple requests together
- Async batch processing
- Trade latency for cost

#### Quantization
- INT4/INT8 quantization for self-hosted models
- Reduced memory footprint
- Minimal quality loss

### 5. Security

#### Prompt Injection Defense
- Input sanitization
- Instruction hierarchy enforcement
- Detection classifiers
- Sandboxed execution

#### PII Handling
- Detect and mask PII before sending to LLM APIs
- Presidio (Microsoft's PII library)
- GDPR/CCPA compliance in AI pipelines

#### RBAC for AI
- Role-based access to agent capabilities
- Audit logging all AI interactions
- Secrets management (never in prompts)

### 6. Cloud Deployment

#### AWS Bedrock
- Managed LLM inference on AWS
- Fine-tuning on Bedrock
- Guardrails for Bedrock

#### GCP Vertex AI
- Vertex AI Agent Builder
- Managed RAG on Google Cloud
- Gemini API on Vertex

#### Azure OpenAI
- Enterprise OpenAI with compliance
- Private deployments
- Content filtering

### 7. CI/CD for AI

- Automated eval runs on prompt changes
- Regression testing for agent behavior
- Canary deployments for new model versions
- GitHub Actions for AI pipelines
- Eval-gated deployments (don't ship if scores drop)

---

## 📚 Learning Resources

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| Full Stack LLM Bootcamp | Course (Free) | ⭐⭐⭐ | https://fullstackdeeplearning.com/llm-bootcamp |
| Chip Huyen: AI Engineering Book | Book | ⭐⭐⭐ | https://huyenchip.com |
| LangSmith Documentation | Docs | ⭐⭐⭐ | https://docs.smith.langchain.com |
| FastAPI Documentation | Docs | ⭐⭐⭐ | https://fastapi.tiangolo.com |
| vLLM Documentation | Docs | ⭐⭐ | https://docs.vllm.ai |
| GPTCache GitHub | GitHub | ⭐⭐ | https://github.com/zilliztech/GPTCache |
| Microsoft Presidio | GitHub | ⭐⭐ | https://github.com/microsoft/presidio |

---

## 🏗️ Capstone Project: Production Multi-Agent SaaS

**What it does**: A production-grade web application powered by a multi-agent backend.

**Features**:
- [ ] Multi-agent backend (at least 3 specialized agents)
- [ ] FastAPI REST API with streaming
- [ ] Simple React/Streamlit frontend
- [ ] LangSmith tracing for every request
- [ ] Semantic caching (Redis + embeddings)
- [ ] Model routing (cheap for simple, expensive for complex)
- [ ] PII detection before LLM calls
- [ ] Docker containerization
- [ ] CI/CD pipeline with eval gating
- [ ] Load tested at 100 concurrent users

**Location**: `projects/phase-5-production-saas/`  
**Tech Stack**: FastAPI, LangGraph, OpenAI, LangSmith, Redis, Docker, GitHub Actions

---

## 🏗️ Hands-On Exercises

- [ ] Deploy an agent API with FastAPI + Docker
- [ ] Set up LangSmith tracing on an existing project
- [ ] Implement semantic caching — measure cost reduction
- [ ] Build a model router that selects model based on query complexity
- [ ] Add PII masking to an LLM pipeline
- [ ] Write an automated eval pipeline that runs on git push
- [ ] Load test with Locust at 100 concurrent users

---

## ✅ Milestone Checkpoints

- [ ] Production AI API deployed and publicly accessible
- [ ] All requests traced end-to-end in LangSmith
- [ ] Semantic caching reduces costs by 40%+
- [ ] Passes load test: 100 concurrent users, P95 < 5s
- [ ] Automated eval pipeline running in CI/CD
- [ ] PII detection active on all user inputs

---

## 📝 LinkedIn Articles (This Phase)

### Article 18: "LLMOps is Different from MLOps — Here's What Changed"
**Draft**: `notes/articles/article-18-llmops.md`  
**Post When**: Week 25

### Article 19: "I Reduced My AI App Costs by 60% With Semantic Caching"
**Draft**: `notes/articles/article-19-semantic-caching.md`  
**Post When**: Week 26

### Article 20: "How to Make Your AI Agent Production-Ready"
**Draft**: `notes/articles/article-20-production-agents.md`  
**Post When**: Week 27

### Article 21: "6 Months Learning AI Engineering in Public — My Full Review"
**Draft**: `notes/articles/article-21-6month-review.md`  
**Post When**: Week 28 (final week!)

---

## 🔗 Key References

- [ML Engineering for Production Specialization — Coursera](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)
- [LLM in Production — Full Stack Deep Learning](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/)
- [Production AI Checklist — Anthropic](https://docs.anthropic.com/en/docs/about-claude/models/overview)
