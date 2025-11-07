
import math

hte = 100
hre = 2
fc = 900
d = 4
a_hre = (3.2*(math.log10(11.75*hre))**2)-4.97
Lp = 69.55 + 26.16*math.log10(fc) - 13.82*math.log10(hte) - \
    a_hre + ((44.9 - 6.55*math.log10(hte))*math.log10(d))
print(f'Lp = {Lp:7.2f} dB')
