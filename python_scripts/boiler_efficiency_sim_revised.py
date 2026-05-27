"""
Boiler Efficiency Calculation - Revised with Air Preheater
"""

# HFO elemental composition (mass fractions)
C = 84.0 / 100
H = 13.4 / 100
S = 0.6 / 100
O = 1.5 / 100
N = 0.5 / 100
W = 1.0 / 100

# Fuel and heating value
G_fuel = 52.25 / 3.6  # ton/h → kg/s
LHV = 38333.68  # kJ/kg
Q_fuel_input = G_fuel * LHV  # kW

# Steam side
h_steam = 3400.8  # kJ/kg  H02603
h_feedwater = 1097.1  # kJ/kg  H02448
G_steam = 716.17 / 3.6  # ton/h → kg/s
Q_steam = G_steam * (h_steam - h_feedwater)  # kW

# Excess air from O2 measurement (Siegert method)
O2_measured = 0.75  # vol% dry flue gas — X02419
lambda_excess = 21 / (21 - O2_measured)
excess_air_pct = (lambda_excess - 1) * 100

print(f"O2 in flue gas        : {O2_measured:.2f} vol%")
print(f"Excess air factor (λ) : {lambda_excess:.4f}")
print(f"Excess air            : {excess_air_pct:.1f}%")

# Corrected actual air and flue gas flow
air_stoich = (2.667 * C + 8 * (H - O / 8) + S) / 0.232
air_actual = air_stoich * lambda_excess  # kg/kg fuel

CO2 = 3.667 * C
SO2 = 2.0 * S
H2O = 9.0 * H + W
N2_fuel = N
N2_air = air_actual * 0.768
excess_O2 = air_actual * 0.232 - (2.667 * C + 8 * (H - O / 8) + S)

G_fg_per_kg = CO2 + SO2 + H2O + N2_fuel + N2_air + excess_O2
G_fluegas = G_fuel * G_fg_per_kg

print(f"\nActual air flow       : {air_actual:.3f} kg/kg fuel")
print(f"Flue gas yield        : {G_fg_per_kg:.3f} kg/kg fuel")
print(f"Flue gas flow         : {G_fluegas:.2f} kg/s")

# Heat flows
Cp_fluegas = 1.10  # kJ/kg·K
T_ref = 25.0  # °C
T_stack = 141.57  # °C — T02114 rotary air preheater gas outlet

Q_stack_loss = G_fluegas * Cp_fluegas * (T_stack - T_ref)
eta_steam = Q_steam / Q_fuel_input
eta_APH = (Q_fuel_input - Q_stack_loss) / Q_fuel_input

print(f"\nTrue stack temperature : {T_stack:.2f} °C")
print(f"Stack heat loss        : {Q_stack_loss:.1f} kW")
print(f"Stack loss (% of LHV)  : {Q_stack_loss / Q_fuel_input * 100:.1f}%")
print(f"\nBoiler efficiency (steam/fuel) : {eta_steam:.1%}")
print(f"Boiler efficiency (APH method) : {eta_APH:.1%}")