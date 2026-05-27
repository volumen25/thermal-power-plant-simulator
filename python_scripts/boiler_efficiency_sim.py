"""
Boiler Efficiency Calculation — Direct Method
Thermal Power Plant Simulator Course

Method: Direct (input/output)
    η = Q_steam / Q_fuel = G_steam × (h_steam - h_fw) / (G_fuel × LHV)

Measurement boundary:
    - Feedwater inlet : T02447 / H02448 (economizer water inlet)
    - Steam outlet    : T02602 / H02603 (HP line steam)
    - Fuel supply     : G01038 (HFO supply flow to boiler)

References:
    - IAPWS-IF97 steam tables via iapws library
    - Dulong formula for LHV from elemental composition
"""

# ---------------------------------------------------------------------------
# HFO Properties
# ---------------------------------------------------------------------------

# Elemental composition (mass fractions) — X008xx tags
C = 84.0 / 100  # X00800 carbon
H = 13.4 / 100  # X00801 hydrogen
S = 0.6 / 100   # X00802 sulfur
O = 1.5 / 100   # X00803 oxygen
N = 0.5 / 100   # X00804 nitrogen
W = 1.0 / 100   # X00807 moisture

# Heating values (kJ/kg)
HHV = 41303.16  # H00810 — HFO heat value from simulator
# Dulong formula: LHV = HHV - latent heat of moisture formed
# 2442 kJ/kg = latent heat of water vapour at 25°C
# 9H = water formed per kg fuel from hydrogen combustion
LHV = HHV - 2442 * (9 * H + W)  # 38333.68 kJ/kg

# ---------------------------------------------------------------------------
# Measurement Data (simulator snapshot)
# ---------------------------------------------------------------------------

# Steam side
h_steam = 3400.8    # kJ/kg  H02603  HP line steam enthalpy
h_fw = 1097.1       # kJ/kg  H02448  economizer water inlet enthalpy
G_steam = 716.17 / 3.6  # kg/s  G02600  HP line steam flow (ton/h → kg/s)

# Fuel side
G_fuel = 52.42 / 3.6    # kg/s  G01038  HFO supply flow to boiler (ton/h → kg/s)

# Flue gas — for indirect verification
O2_fg = 0.75        # vol%   X02419  O2 in flue gas (dry)
T_stack = 141.57    # °C     T02114  rotary air preheater gas outlet
T_ref = 25.0        # °C     reference temperature

# ---------------------------------------------------------------------------
# Direct Method
# ---------------------------------------------------------------------------

Q_steam = G_steam * (h_steam - h_fw)    # kW — heat absorbed by steam
Q_fuel = G_fuel * LHV                   # kW — heat released by fuel (LHV basis)
eta_direct = Q_steam / Q_fuel

# ---------------------------------------------------------------------------
# Indirect Method (stack loss only)
# ---------------------------------------------------------------------------

# Excess air from O2 measurement (Siegert method)
lambda_excess = 21 / (21 - O2_fg)
air_stoich = (2.667 * C + 8 * (H - O / 8) + S) / 0.232  # kg/kg fuel
air_actual = air_stoich * lambda_excess                    # kg/kg fuel

# Flue gas composition (kg/kg fuel)
fg_CO2 = 3.667 * C
fg_SO2 = 2.0 * S
fg_H2O = 9.0 * H + W
fg_N2 = N + air_actual * 0.768
fg_O2_excess = air_actual * 0.232 - (2.667 * C + 8 * (H - O / 8) + S)
G_fg_per_kg = fg_CO2 + fg_SO2 + fg_H2O + fg_N2 + fg_O2_excess

G_fluegas = G_fuel * G_fg_per_kg    # kg/s
Cp_fg = 1.10                        # kJ/kg·K — approximate mean Cp

Q_stack = G_fluegas * Cp_fg * (T_stack - T_ref)    # kW — stack heat loss
eta_indirect = (Q_fuel - Q_stack) / Q_fuel

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

print("=" * 55)
print("  Boiler Efficiency Calculation")
print("=" * 55)

print("\n--- Fuel Properties ---")
print(f"  HHV                    : {HHV:.2f} kJ/kg")
print(f"  LHV (Dulong)           : {LHV:.2f} kJ/kg")
print(f"  HHV - LHV              : {HHV - LHV:.2f} kJ/kg")

print("\n--- Mass Flows ---")
print(f"  Steam flow  (G02600)   : {G_steam:.4f} kg/s")
print(f"  Fuel flow   (G01038)   : {G_fuel:.4f} kg/s")
print(f"  Flue gas flow          : {G_fluegas:.2f} kg/s")

print("\n--- Heat Flows ---")
print(f"  Heat to steam          : {Q_steam:.1f} kW")
print(f"  Fuel heat input (LHV)  : {Q_fuel:.1f} kW")
print(f"  Stack heat loss        : {Q_stack:.1f} kW")
print(f"  Stack loss             : {Q_stack / Q_fuel * 100:.1f}% of LHV")

print("\n--- Combustion ---")
print(f"  Excess air factor (λ)  : {lambda_excess:.4f}")
print(f"  Excess air             : {(lambda_excess - 1) * 100:.1f}%")
print(f"  Stack temperature      : {T_stack:.2f} °C")

print("\n--- Boiler Efficiency ---")
print(f"  Direct method          : {eta_direct:.1%}")
print(f"  Indirect method        : {eta_indirect:.1%}")
print(f"  Difference             : {abs(eta_indirect - eta_direct) * 100:.1f} pp")
print("=" * 55)
