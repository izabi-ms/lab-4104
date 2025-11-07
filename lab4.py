
import math

blocking_probability = 2/100  # GOS
population = 2_000_000
Au = (2/60)*3  # 2 calls/hr, 3 min avg => 0.1 Erlang/user

# System A
C1 = 19
A1 = 12
U1 = A1/Au
Aa = U1*394
percentage_A = (Aa/population)*100

# System B
C2 = 57
A2 = 45
U2 = A2/Au
Bb = U2*98
percentage_B = (Bb/population)*100

# System C
C3 = 100
A3 = 88
U3 = A3/Au
Cc = U3*49
percentage_C = (Cc/population)*100

T = Aa + Bb + Cc
percentage_T = (T/population)*100

print(f"System A subscribers: {Aa:.0f}, penetration: {percentage_A:.2f}%")
print(f"System B subscribers: {Bb:.0f}, penetration: {percentage_B:.2f}%")
print(f"System C subscribers: {Cc:.0f}, penetration: {percentage_C:.2f}%")
print(f"Total subscribers: {T:.0f}, penetration: {percentage_T:.2f}%")
