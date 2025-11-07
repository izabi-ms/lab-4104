# required_db = int(input("Enter required SIR in dB: "))
# SIR = 10**(required_db/10)
# # n = int(input("Enter path loss exponent n (typically 2 to 4): "))
# vals = []
# for i in range(0,8):
#     for j in range(0,8):
#         N = i*i + i*j + j*j
#         if N > 0 and N not in vals:
#             vals.append(N)
# vals.sort()

# for n in [4, 3]:
#     factor = 3**(n/2)
#     theoretical_N = ((6 * SIR) / factor) ** (2.0 / n)
#     chosen = None
#     for v in vals:
#         if v >= theoretical_N:
#             chosen = v
#             break
#     print("n =", n)
#     print("theoretical N =", theoretical_N)
#     print("chosen cluster size N =", chosen)
#     print("frequency reuse factor = 1/", chosen, "=", 1.0/chosen)



SIR_dB=15.0
i0=6.0
L=10**(SIR_dB/10.0)
T=i0*L
# A=[1,3,4,7,9,12,13,16,19,21,27,28,31,36,37]
A = []
for i in range(0,8):
    for j in range(0,8):
        N = i*i + i*j + j*j
        if N > 0 and N not in A:
            A.append(N)
A.sort()
n=4.0
Q=T**(1.0/n)
x=(Q*Q)/3.0
i=0
while True:
    if A[i]>=x:
        N=A[i]
        break
    i=i+1
print("n=4 -> N=",N," reuse=",f"{1.0/N:.6f}")

n=3.0
Q=T**(1.0/n)
x=(Q*Q)/3.0
i=0
while True:
    if A[i]>=x:
        N=A[i]
        break
    i=i+1
print("n=3 -> N=",N," reuse=",f"{1.0/N:.6f}")
