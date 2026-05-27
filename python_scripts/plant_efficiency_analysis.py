"""
Plant Efficiency Analysis with Visualization
For Thermal Power Plant Simulator Course
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_efficiency_curve():
    """
    Plot thermal efficiency vs plant load.

    Data is illustrative — representative of a mid-size
    coal-fired plant under varying load conditions.
    """
    # Illustrative data: load (%) vs thermal efficiency (%)
    load = np.array([30, 40, 50, 60, 70, 80, 90, 100])
    efficiency = np.array([32, 35, 37, 38.5, 39.5, 40, 39.8, 39])

    peak_efficiency = efficiency.max()
    peak_load = load[efficiency.argmax()]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(load, efficiency, "bo-", linewidth=2, markersize=8)
    ax.axhline(
        y=peak_efficiency,
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"Peak efficiency: {peak_efficiency:.1f}% at {peak_load}% load",
    )
    ax.set_title("Thermal Power Plant Efficiency vs Load")
    ax.set_xlabel("Plant Load (%)")
    ax.set_ylabel("Thermal Efficiency (%)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    output_path = "efficiency_curve.png"
    fig.savefig(output_path, dpi=150)
    print(f"Efficiency curve saved as '{output_path}'")
    print(f"Peak efficiency: {peak_efficiency:.1f}% at {peak_load}% load")


if __name__ == "__main__":
    plot_efficiency_curve()