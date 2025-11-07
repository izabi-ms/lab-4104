
import math

pt = 50
fc = 900
gt = 1
gr = 1
d = 100
L = 1

lam = (3*10e8)/(fc*10e6)

tr_dBm = math.ceil(10*math.log10(pt*1000))
tr_dBW = math.ceil(10*math.log10(pt))

c = ((pt*gt*gr*(lam**2))/(((4*3.1416)**2)*(d**2)*L))*1000
Pr = 10*math.log10(c)

d2 = Pr + (20*math.log10(100/10000))

print(f"Transmit power: {tr_dBm} dBm, {tr_dBW} dBW")
print(f"Rx power at 100 m: {Pr:.2f} dBm")
print(f"Rx power at 10 km: {d2:.2f} dBm")
