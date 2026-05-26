"""
Basic Rankine Cycle Efficiency Calculation
For Thermal Power Plant Simulator Course
"""

import numpy as np

def rankine_cycle_efficiency(t_boiler=500, t_condenser=30, p_boiler=100, p_condenser=0.1):
    """Simple ideal Rankine cycle efficiency calculation"""
    # Temperatures in Kelvin
    T_hot = t_boiler + 273
    T_cold = t_condenser + 273
    
    # Carnot efficiency as upper bound (for illustration)
    eta_carnot = 1 - T_cold / T_hot
    
    # Typical Rankine efficiency (approx 30-40% for real plants)
    eta_rankine = eta_carnot * 0.65  # Rough factor
    
    print(f"Boiler Temperature: {t_boiler}°C")
    print(f"Condenser Temperature: {t_condenser}°C")
    print(f"Carnot Efficiency: {eta_carnot:.1%}")
    print(f"Estimated Rankine Efficiency: {eta_rankine:.1%}")
    
    return eta_rankine

if __name__ == "__main__":
    rankine_cycle_efficiency()
