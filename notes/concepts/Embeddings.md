---
tags: [#concept, #foundations, #embeddings, #rag]
related: [[Linear-Algebra-and-Vectors]], [[Transformers]], [[Vector Databases]]
phase: 0
---

# Embeddings

## What is it?
An embedding is a mapping of discrete items (words, sentences, images, audio) into continuous, dense numerical vectors in a high-dimensional space where semantic meaning translates directly into geometric distance.

## Why does it matter?
- Traditional keyword search (like BM25 or SQL `LIKE '%apple%'`) cannot understand synonyms, context, or semantic intent.
- With embeddings, "How do I fix a flat tire?" and "Steps to repair bicycle puncture" are placed close together in vector space despite having few identical words.
- In RAG (Retrieval-Augmented Generation) and Agent Tool Selection, embeddings allow agents to recall relevant memory, documentation, and tools by semantic proximity.

## How it works
1. **Model**: An encoder model (like BERT, text-embedding-3, or BGE) processes text tokens.
2. **Dense Vector Output**: The model outputs a vector, e.g. of dimension $d = 768$ or $1536$.
3. **Distance Metrics**:
   - **Cosine Similarity**: Value from -1 to 1 (1 = identical direction).
   - **Euclidean Distance ($L_2$)**: Straight-line distance in Euclidean space.
   - **Dot Product**: Equivalent to cosine similarity when vectors are $L_2$-normalized.

## The Vector Math of Semantics
A famous demonstration of vector arithmetic in embeddings:
$$\vec{v}_{\text{King}} - \vec{v}_{\text{Man}} + \vec{v}_{\text{Woman}} \approx \vec{v}_{\text{Queen}}$$

This proves that embeddings capture latent abstract properties (gender, royalty, tense) as directional geometric offsets.

## Related Concepts
- [[Linear-Algebra-and-Vectors]]
- [[Tokenization]]
- [[Vector Databases]]
- [[Retrieval-Augmented Generation]]
