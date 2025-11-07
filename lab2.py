
import math
import ast

r_si = 15
i0 = 6

for n in [4, 3]:
    N = 7
    Q = math.sqrt(3*N)
    si = 10*(math.log10((Q**n)/i0))
    if si < r_si:
        i = 2
        j = 2
        N = (i*i) + (i*j) + (j*j)  # 12
        Q = math.sqrt(3*N)
        si = 10*(math.log10((Q**n)/i0))
    print(f'For n = {n}: S/I={si:7.3f} dB, N={N}, Q={Q:7.3f}')
