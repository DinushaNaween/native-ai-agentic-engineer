"""
Performance Benchmark: Pure Python Loops vs NumPy BLAS/SIMD Vectorization.

Demonstrates why vectorized linear algebra libraries are essential for
training and running neural networks and processing embeddings.
"""

import time
import random
import sys
from pathlib import Path

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from matrix_ops import dot_product, matrix_multiply
import numpy as np


def benchmark_dot_product(dim: int = 200_000):
    print(f"\n--- 1. Dot Product Benchmark ({dim:,} dimensions) ---")
    u_list = [random.random() for _ in range(dim)]
    v_list = [random.random() for _ in range(dim)]
    
    u_np = np.array(u_list)
    v_np = np.array(v_list)
    
    # Pure Python
    t0 = time.perf_counter()
    res_py = dot_product(u_list, v_list)
    t_py = time.perf_counter() - t0
    
    # NumPy
    t0 = time.perf_counter()
    res_np = float(np.dot(u_np, v_np))
    t_np = time.perf_counter() - t0
    
    speedup = t_py / t_np if t_np > 0 else 0
    print(f"Pure Python dot product: {t_py * 1000:.2f} ms")
    print(f"NumPy dot product:       {t_np * 1000:.2f} ms")
    print(f"Speedup with NumPy:      {speedup:.1f}x faster 🚀")


def benchmark_matrix_multiply(size: int = 150):
    print(f"\n--- 2. Matrix Multiplication Benchmark ({size}x{size} matrices) ---")
    A_list = [[random.random() for _ in range(size)] for _ in range(size)]
    B_list = [[random.random() for _ in range(size)] for _ in range(size)]
    
    A_np = np.array(A_list)
    B_np = np.array(B_list)
    
    # Pure Python
    t0 = time.perf_counter()
    res_py = matrix_multiply(A_list, B_list)
    t_py = time.perf_counter() - t0
    
    # NumPy
    t0 = time.perf_counter()
    res_np = np.matmul(A_np, B_np)
    t_np = time.perf_counter() - t0
    
    speedup = t_py / t_np if t_np > 0 else 0
    print(f"Pure Python matrix mult: {t_py:.4f} seconds")
    print(f"NumPy matrix mult:       {t_np:.4f} seconds")
    print(f"Speedup with NumPy:      {speedup:.1f}x faster 🚀")


if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Phase 0 Foundations: Linear Algebra Performance Benchmark")
    print("=" * 60)
    benchmark_dot_product()
    benchmark_matrix_multiply()
    print("\n✅ Key Takeaway: Vectorization leverages hardware SIMD & BLAS,")
    print("   which is fundamental to scaling LLMs and high-dimensional embeddings.")
