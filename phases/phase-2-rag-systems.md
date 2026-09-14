# Phase 2 — RAG Systems (Retrieval-Augmented Generation)
**Duration**: Weeks 9–12 (Nov 9 – Dec 6, 2026)  
**Status**: 🔲 Not Started

> Make LLMs know things they weren't trained on — connect them to your data.

---

## 🎯 Learning Topics

### 1. Embeddings
- What embeddings are (vectors representing meaning)
- Cosine similarity and distance metrics
- Embedding models: text-embedding-3-small, all-MiniLM, BGE
- Sentence transformers library
- How embeddings enable semantic search

### 2. Vector Databases
- What vector databases are and why you need them
- **Chroma** — local, easy to start with
- **Pinecone** — managed cloud solution
- **Qdrant** — open-source, performant
- **Weaviate** — schema-based, multimodal
- **pgvector** — Postgres extension (simplest for existing PG users)
- CRUD operations in vector DBs

### 3. Chunking Strategies
- Fixed-size chunking (character/token count)
- Sentence-based chunking
- Semantic chunking (split by meaning)
- Hierarchical chunking (parent-child)
- Sliding window with overlap
- Document-specific strategies (PDF, code, HTML)

### 4. Retrieval Techniques
- **Dense retrieval** — embedding similarity (ANN search)
- **Sparse retrieval** — BM25, keyword matching
- **Hybrid search** — combining dense + sparse with RRF
- Re-ranking with cross-encoders
- Maximum Marginal Relevance (MMR) for diversity

### 5. RAG Pipeline (Full Flow)
```
Documents → Chunk → Embed → Store in VectorDB
                                    ↓
Query → Embed → Retrieve Top-K → Augment Prompt → LLM → Answer
```

### 6. Advanced RAG Techniques
- **HyDE** — Hypothetical Document Embeddings
- **FLARE** — Forward-Looking Active Retrieval
- **GraphRAG** — Knowledge graph + RAG
- **Multi-query retrieval** — generate multiple query variants
- **Query rewriting** — improve query before retrieval
- **Contextual compression** — compress retrieved docs

### 7. RAG Evaluation with RAGAS
- **Faithfulness** — is the answer grounded in the context?
- **Answer Relevance** — does the answer address the question?
- **Context Precision** — are retrieved docs relevant?
- **Context Recall** — did we retrieve all needed info?

---

## 📚 Learning Resources

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| DeepLearning.AI: Building and Evaluating Advanced RAG | Course (Free) | ⭐⭐⭐ | https://deeplearning.ai/short-courses |
| LangChain RAG Tutorial | Docs | ⭐⭐⭐ | https://python.langchain.com/docs/tutorials/rag |
| LlamaIndex RAG Guide | Docs | ⭐⭐⭐ | https://docs.llamaindex.ai |
| Pinecone Learning Center | Articles | ⭐⭐⭐ | https://pinecone.io/learn |
| RAGAS Framework | GitHub | ⭐⭐⭐ | https://github.com/explodinggradients/ragas |
| Chroma Docs | Docs | ⭐⭐ | https://docs.trychroma.com |
| Advanced RAG (Weaviate Blog) | Blog Series | ⭐⭐ | https://weaviate.io/blog |

---

## 🏗️ Phase Project: Personal Knowledge RAG

**What it does**: Chat with your own notes, PDFs, and documents.

**Features to build**:
- [ ] Ingest PDF, TXT, Markdown files
- [ ] Chunk documents intelligently
- [ ] Embed and store in ChromaDB locally
- [ ] Retrieve relevant chunks for a query
- [ ] Generate answer with GPT-4o using retrieved context
- [ ] Simple CLI or Streamlit UI
- [ ] Add hybrid search (dense + BM25)
- [ ] Evaluate with RAGAS

**Location**: `projects/phase-2-personal-rag/`

**Tech Stack**: Python, LangChain, ChromaDB, OpenAI, Streamlit, RAGAS

---

## 🏗️ Hands-On Exercises

- [ ] Build RAG pipeline from scratch (no framework) to understand internals
- [ ] Build the same with LangChain
- [ ] Build the same with LlamaIndex
- [ ] Compare Chroma vs Pinecone for the same dataset
- [ ] Implement hybrid search combining dense + BM25
- [ ] Evaluate your RAG with RAGAS and document findings

---

## ✅ Milestone Checkpoints

- [ ] Built a full RAG pipeline from scratch
- [ ] Ingested and queried at least 10 documents
- [ ] Implemented hybrid search
- [ ] RAGAS scores: Faithfulness > 0.8, Answer Relevance > 0.8
- [ ] Deployed Personal Knowledge RAG with a UI

---

## 📝 LinkedIn Articles (This Phase)

### Article 6: "What is RAG? A Visual Explanation for Developers"
**Draft**: `notes/articles/article-06-what-is-rag.md`  
**Post When**: Week 9

### Article 7: "I Built My Own RAG System — Here's What I Learned"
**Draft**: `notes/articles/article-07-built-rag.md`  
**Post When**: Week 11

### Article 8: "Why Your RAG Pipeline Lies to You (and How to Fix It)"
**Draft**: `notes/articles/article-08-rag-failures.md`  
**Post When**: Week 12

### Article 9: "Vector Databases Explained: Pinecone vs Chroma vs pgvector"
**Draft**: `notes/articles/article-09-vector-dbs.md`  
**Post When**: Week 10

---

## 🔗 Key Papers

- [RAG: Retrieval-Augmented Generation (2020)](https://arxiv.org/abs/2005.11401) — Original RAG paper
- [HyDE: Precise Zero-Shot Dense Retrieval](https://arxiv.org/abs/2212.10496)
- [GraphRAG (Microsoft)](https://arxiv.org/abs/2404.16130)
- [RAGAS Evaluation Framework](https://arxiv.org/abs/2309.15217)
