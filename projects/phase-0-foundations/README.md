# Phase 0 Foundations: Linear Algebra & Vector Embeddings

This project contains the foundational mathematics and hands-on Python implementations for **Phase 0: ML & AI Foundations**.

---

## 📁 Directory Layout

```
projects/phase-0-foundations/
├── .venv/                      # Isolated Python 3.13 virtual environment
├── requirements.txt            # Core dependencies (numpy, matplotlib, pandas, pytest, ipykernel)
├── src/
│   ├── matrix_ops.py          # Pure Python dot product, norm, cosine similarity, & matrix multiplication
│   └── semantic_search.py     # Mini vector store demonstrating semantic retrieval
├── tests/
│   └── test_matrix_ops.py     # Unit tests verifying scratch math vs NumPy
├── exercises/
│   ├── run_benchmarks.py      # Benchmark: Pure Python vs NumPy BLAS/SIMD (1000x+ speedup)
│   └── visualize_embeddings.py# Visualizes vector angles and semantic clusters
└── assets/
    └── vector_space_plot.png  # Generated 2D geometric and semantic space plot
```

---

## 🚀 Quickstart

### 1. Activate Environment
```bash
source projects/phase-0-foundations/.venv/bin/activate
```

### 2. Run Unit Tests
Verify that all scratch linear algebra algorithms match NumPy:
```bash
pytest projects/phase-0-foundations/tests/
```

### 3. Run Benchmark (Pure Python vs NumPy Vectorization)
```bash
python projects/phase-0-foundations/exercises/run_benchmarks.py
```

### 4. Generate Vector Plots
```bash
python projects/phase-0-foundations/exercises/visualize_embeddings.py
```

---

## 💡 Key Conceptual Takeaways
- **Dot Product ($\vec{u} \cdot \vec{v}$)**: Projects one vector onto another. Used in attention mechanisms ($QK^T$) and semantic similarity.
- **Cosine Similarity**: Normalizes for length ($\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$), isolating directional angle.
- **Hardware Acceleration**: Pure Python nested loops take $\mathcal{O}(M \times K \times N)$ on the CPU interpreter. NumPy delegates to underlying BLAS/LAPACK routines utilizing CPU SIMD registers, yielding >1000x speedups.
