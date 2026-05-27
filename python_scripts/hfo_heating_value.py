# HFO elemental composition (mass fractions)
C  = 84.0  / 100
H  = 13.4  / 100
S  = 0.6   / 100
O  = 1.5   / 100
N  = 0.5   / 100
ash  = 1.0 / 100
slag = 0.3 / 100
W  = 1.0   / 100     # moisture

HHV = 41303.15       # kJ/kg (H00810)

# Dulong formula: LHV from HHV
# 9H accounts for water formed by hydrogen combustion
LHV = HHV - 2442 * (9 * H + W)

print(f"HHV : {HHV:.2f} kJ/kg")
print(f"LHV : {LHV:.2f} kJ/kg")
print(f"Difference (HHV - LHV): {HHV - LHV:.2f} kJ/kg")