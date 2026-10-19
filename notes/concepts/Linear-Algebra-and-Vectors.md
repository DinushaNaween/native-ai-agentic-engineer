---
tags: [#concept, #foundations, #math, #linear-algebra]
related: [[Embeddings]], [[Neural Networks]], [[Transformers]]
phase: 0
---

# Linear Algebra & Vectors for AI

## What is it?
Linear algebra is the mathematical language of machine learning and AI. In modern AI, data (text, images, audio, user behavior) is converted into numerical lists called **vectors**, grids called **matrices**, and higher-dimensional arrays called **tensors**.

## Core Mathematical Entities
1. **Scalar**: A single number (e.g., $s = 4.2$) — rank 0 tensor.
2. **Vector**: An ordered list of numbers with direction and magnitude in $n$-dimensional space (e.g., $\vec{v} = [x_1, x_2, \dots, x_n]$) — rank 1 tensor.
3. **Matrix**: A 2D table of numbers representing linear transformations or batches of vectors (e.g., shape $(M, N)$) — rank 2 tensor.
4. **Tensor**: An $N$-dimensional array generalizing scalars, vectors, and matrices.

## Why does it matter for AI Agents & LLMs?
1. **Vector Embeddings**: LLMs cannot read text directly; words, sentences, or chunks are mapped into high-dimensional vector spaces (e.g., 1536 dimensions in OpenAI `text-embedding-3-small` or 768 dimensions in BERT).
2. **Semantic Similarity**: The **Dot Product** and **Cosine Similarity** calculate how closely related two concepts, documents, or agent tool outputs are in vector space.
3. **Neural Network Transformations**: Every neural layer (like $y = Wx + b$) is simply a matrix multiplication followed by vector addition and non-linear activation.

## Key Operations
- **Dot Product**: $\vec{u} \cdot \vec{v} = \sum_{i=1}^n u_i v_i = \|\vec{u}\| \|\vec{v}\| \cos(\theta)$
  - Measures directional alignment. If positive, vectors point in similar directions; if 0, orthogonal (unrelated); if negative, opposite directions.
- **Euclidean Norm (Magnitude)**: $\|\vec{v}\| = \sqrt{\sum_{i=1}^n v_i^2}$
- **Cosine Similarity**: $\text{sim}(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$
  - Normalizes for vector length so only angle/direction (semantic meaning) matters.

## My Analogy / ELI5
> Imagine every concept in human language placed in a giant 3D room. "King" sits near "Queen", while "Apple" sits near "Orange". A vector is simply the GPS coordinates $(x, y, z, \dots)$ of where that concept lives in thought-space. The dot product is the distance and compass angle between any two thoughts.

## Related Concepts
- [[Embeddings]]
- [[Neural Networks]]
- [[Transformers]]
- [[Attention Mechanism]]
