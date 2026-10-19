"""
Visualizing Vectors, Angles, and Semantic Embedding Spaces.

Generates visual representations of:
1. 2D Vector Geometry (Direction, Norm, and Angle theta)
2. Semantic Concept Clustering in Vector Space
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def plot_vector_geometry(output_path: Path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#0f172a')
    
    # ---------------- Subplot 1: Vector Angles & Dot Product ----------------
    ax1.set_facecolor('#1e293b')
    ax1.axhline(0, color='#475569', linewidth=1, linestyle='--')
    ax1.axvline(0, color='#475569', linewidth=1, linestyle='--')
    
    u = np.array([3.0, 1.5])
    v = np.array([1.5, 3.5])
    w = np.array([-2.5, 2.0])
    
    # Draw arrows
    ax1.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='#38bdf8', label=r'Vector $\vec{u}$')
    ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='#4ade80', label=r'Vector $\vec{v}$ (similar angle)')
    ax1.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='#f43f5e', label=r'Vector $\vec{w}$ (divergent)')
    
    ax1.set_xlim(-4, 5)
    ax1.set_ylim(-1, 5)
    ax1.set_title("Vector Angles & Directionality", color='#f8fafc', fontsize=14, fontweight='bold', pad=12)
    ax1.tick_params(colors='#94a3b8')
    for spine in ax1.spines.values():
        spine.set_color('#334155')
    ax1.legend(facecolor='#0f172a', edgecolor='#334155', labelcolor='#f8fafc', loc='upper right')
    ax1.grid(True, linestyle=':', alpha=0.3, color='#94a3b8')
    
    # ---------------- Subplot 2: Conceptual Embeddings Space ----------------
    ax2.set_facecolor('#1e293b')
    
    clusters = {
        "AI / Agents": {
            "color": "#38bdf8",
            "points": [
                ("LLM", [2.8, 3.2]),
                ("AI Agent", [3.2, 3.5]),
                ("Prompt", [2.5, 2.9]),
                ("RAG", [3.5, 2.8]),
            ]
        },
        "Food / Culinary": {
            "color": "#fb923c",
            "points": [
                ("Pizza", [-3.0, -1.8]),
                ("Pasta", [-2.8, -2.2]),
                ("Burger", [-3.5, -1.5]),
            ]
        },
        "Pets / Animals": {
            "color": "#a855f7",
            "points": [
                ("Dog", [-1.5, 3.0]),
                ("Puppy", [-1.3, 3.4]),
                ("Cat", [-1.8, 2.6]),
            ]
        }
    }
    
    for category, data in clusters.items():
        xs = [pt[1][0] for pt in data["points"]]
        ys = [pt[1][1] for pt in data["points"]]
        ax2.scatter(xs, ys, color=data["color"], s=120, label=category, edgecolors='#ffffff', linewidth=1.5, zorder=3)
        for label, coord in data["points"]:
            ax2.annotate(
                label,
                (coord[0], coord[1]),
                xytext=(0, 9),
                textcoords="offset points",
                ha='center',
                fontsize=11,
                fontweight='semibold',
                color='#f8fafc',
            )
            
    ax2.axhline(0, color='#475569', linewidth=1, linestyle='--')
    ax2.axvline(0, color='#475569', linewidth=1, linestyle='--')
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-4, 5)
    ax2.set_title("Semantic Clustering in Embedding Space", color='#f8fafc', fontsize=14, fontweight='bold', pad=12)
    ax2.tick_params(colors='#94a3b8')
    for spine in ax2.spines.values():
        spine.set_color('#334155')
    ax2.legend(facecolor='#0f172a', edgecolor='#334155', labelcolor='#f8fafc', loc='lower right')
    ax2.grid(True, linestyle=':', alpha=0.3, color='#94a3b8')
    
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"📊 Visualization saved to: {output_path}")


if __name__ == "__main__":
    assets_dir = Path(__file__).parent.parent / "assets"
    out_file = assets_dir / "vector_space_plot.png"
    plot_vector_geometry(out_file)
