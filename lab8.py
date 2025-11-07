
import math

fc = 1.8
hb = 20
d = (math.sqrt(20**2 + 30**2))/1000
Lp = 135.41 + (12.49*math.log10(fc)) - (4.99*math.log10(hb)) + \
    ((46.84 - 2.34*math.log10(hb)) * math.log10(d))
print(f'Lp = {Lp:7.2f} dB')
