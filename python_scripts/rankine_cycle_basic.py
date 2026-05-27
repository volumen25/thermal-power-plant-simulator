"""
Ideal Rankine Cycle Efficiency Calculation
Using IAPWS-IF97 steam tables
For Thermal Power Plant Simulator Course

State points:
    1 - Turbine inlet    (superheated steam, high P, high T)
    2 - Condenser inlet  (wet steam, low P)
    3 - Pump inlet       (saturated liquid, low P)
    4 - Boiler inlet     (compressed liquid, high P)
"""

from iapws import IAPWS97


def rankine_cycle(T_boiler=500, P_boiler=10, P_condenser=0.006):
    """
    Ideal Rankine cycle efficiency using steam tables.

    Parameters
    ----------
    T_boiler    : float  Turbine inlet temperature (°C)
    P_boiler    : float  Boiler pressure (MPa)
    P_condenser : float  Condenser pressure (MPa), default ~36°C saturation

    Returns
    -------
    dict with enthalpies, work, heat, and efficiency
    """
    # State 1: Turbine inlet — superheated steam
    state1 = IAPWS97(T=T_boiler + 273.15, P=P_boiler)

    # State 2: Turbine exit — isentropic expansion (s1 = s2)
    state2 = IAPWS97(P=P_condenser, s=state1.s)

    # State 3: Pump inlet — saturated liquid at condenser pressure
    state3 = IAPWS97(P=P_condenser, x=0)

    # State 4: Boiler inlet — pump exit (isentropic compression, s3 = s4)
    state4 = IAPWS97(P=P_boiler, s=state3.s)

    # Energy balance (kJ/kg)
    w_turbine = state1.h - state2.h
    w_pump = state4.h - state3.h
    q_boiler = state1.h - state4.h
    q_condenser = state2.h - state3.h
    w_net = w_turbine - w_pump
    eta = w_net / q_boiler

    # Turbine exit quality check
    if state2.x is not None:
        quality_str = f"{state2.x:.3f} ({'wet' if state2.x < 1 else 'dry'})"
        if state2.x < 0.85:
            quality_str += " — WARNING: consider reheat cycle"
    else:
        quality_str = "superheated"

    results = {
        "T_boiler_C": T_boiler,
        "P_boiler_MPa": P_boiler,
        "P_condenser_MPa": P_condenser,
        "T_condenser_C": round(state3.T - 273.15, 2),
        "h1_kJ_kg": round(state1.h, 2),
        "h2_kJ_kg": round(state2.h, 2),
        "h3_kJ_kg": round(state3.h, 2),
        "h4_kJ_kg": round(state4.h, 2),
        "w_turbine_kJ_kg": round(w_turbine, 2),
        "w_pump_kJ_kg": round(w_pump, 2),
        "w_net_kJ_kg": round(w_net, 2),
        "q_boiler_kJ_kg": round(q_boiler, 2),
        "q_condenser_kJ_kg": round(q_condenser, 2),
        "eta_thermal": round(eta, 4),
    }

    print(f"\n{'='*45}")
    print("  Rankine Cycle Analysis")
    print(f"{'='*45}")
    print(f"  Boiler:     {T_boiler}°C  |  {P_boiler} MPa")
    print(f"  Condenser:  {results['T_condenser_C']}°C  |  {P_condenser} MPa")
    print(f"{'-'*45}")
    print(f"  h1 (turbine inlet):   {results['h1_kJ_kg']:>8} kJ/kg")
    print(f"  h2 (turbine exit):    {results['h2_kJ_kg']:>8} kJ/kg")
    print(f"  h3 (pump inlet):      {results['h3_kJ_kg']:>8} kJ/kg")
    print(f"  h4 (boiler inlet):    {results['h4_kJ_kg']:>8} kJ/kg")
    print(f"{'-'*45}")
    print(f"  Turbine work:    {results['w_turbine_kJ_kg']:>8} kJ/kg")
    print(f"  Pump work:       {results['w_pump_kJ_kg']:>8} kJ/kg")
    print(f"  Net work:        {results['w_net_kJ_kg']:>8} kJ/kg")
    print(f"  Boiler heat in:  {results['q_boiler_kJ_kg']:>8} kJ/kg")
    print(f"  Turbine exit quality: {quality_str}")
    print(f"{'-'*45}")
    print(f"  Thermal efficiency:   {eta:.1%}")
    print(f"{'='*45}\n")

    return results


if __name__ == "__main__":
    rankine_cycle()
