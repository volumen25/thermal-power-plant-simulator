# Correct boiler boundary — feedwater inlet to boiler
h_feedwater = 1488.99  # kJ/kg  H02452
G_steam = 716.17 / 3.6  # kg/s
h_steam = 3400.8  # kJ/kg  H02603
G_fuel  = 52.25  / 3.6      # ton/h → kg/s

# Heating value (kJ/kg)
HHV = 41303
LHV = 38333.68

Q_steam = G_steam * (h_steam - h_feedwater)
Q_fuel_input = G_fuel * LHV
eta_steam = Q_steam / Q_fuel_input

print(f"Feedwater enthalpy (T02451): {h_feedwater:.2f} kJ/kg")
print(f"Steam enthalpy     (H02603): {h_steam:.2f} kJ/kg")
print(f"Enthalpy rise              : {h_steam - h_feedwater:.2f} kJ/kg")
print(f"Heat to steam              : {Q_steam:.1f} kW")
print(f"Boiler efficiency (direct) : {eta_steam:.1%}")