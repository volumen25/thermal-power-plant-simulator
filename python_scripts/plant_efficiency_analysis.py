"""
Plant Efficiency Analysis with Visualization
For Thermal Power Plant Simulator Course
"""

import numpy as np
import matplotlib.pyplot as plt

# Sample data: Load (%) vs Efficiency (%)
load = np.array([30, 40, 50, 60, 70, 80, 90, 100])
efficiency = np.array([32, 35, 37, 38.5, 39.5, 40, 39.8, 39])

plt.figure(figsize=(10, 6))
plt.plot(load, efficiency, 'bo-', linewidth=2, markersize=8)
plt.title('Thermal Power Plant Efficiency vs Load')
plt.xlabel('Plant Load (%)')
plt.ylabel('Thermal Efficiency (%)')
plt.grid(True, alpha=0.3)
plt.axhline(y=max(efficiency), color='r', linestyle='--', alpha=0.7, label=f'Max Efficiency: {max(efficiency):.1f}%')
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig('efficiency_curve.png')
print("Efficiency curve saved as 'efficiency_curve.png'")
print(f"Maximum efficiency: {max(efficiency):.1f}% at {load[np.argmax(efficiency)]}% load")
