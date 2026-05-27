from iapws import IAPWS97

# --- Measurements ---
P_steam     = 158.48 * 0.1          # bara → MPa
T_steam     = 535.85 + 273.15       # °C → K
P_feedwater = 201.97 * 0.1          # bara → MPa
T_feedwater = 254.47 + 273.15       # °C → K
G_steam     = 716.17 * 1000 / 3600  # ton/h → kg/s

# Fuel flows (ton/h → kg/s)
G_fuel = (9.88 + 14.12 + 14.10 + 14.15) * 1000 / 3600
HHV    = 41303                      # kJ/kg

# --- Steam properties ---
steam     = IAPWS97(T=T_steam,     P=P_steam)
feedwater = IAPWS97(T=T_feedwater, P=P_feedwater)

# --- Energy balance ---
Q_steam = G_steam * (steam.h - feedwater.h)   # kW
Q_fuel  = G_fuel  * HHV                        # kW
eta     = Q_steam / Q_fuel

print(f"HP steam enthalpy      : {steam.h:.2f} kJ/kg")
print(f"Feedwater enthalpy     : {feedwater.h:.2f} kJ/kg")
print(f"Enthalpy rise          : {steam.h - feedwater.h:.2f} kJ/kg")
print(f"Steam flow             : {G_steam:.3f} kg/s")
print(f"Heat to steam          : {Q_steam:.1f} kW")
print(f"Total fuel flow        : {G_fuel:.3f} kg/s")
print(f"Fuel heat input        : {Q_fuel:.1f} kW")
print(f"Boiler efficiency      : {eta:.1%}")