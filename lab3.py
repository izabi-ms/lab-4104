
GOS = 0.5/100
Au = 0.1
A = input("Please enter your numbers, separated by a comma (e.g., 0.005,1.13,3.96): ")
A = [float(x) for x in A.split(",")]
C = input("Please enter the corresponding channels, separated by a comma (e.g., 20,40,60): ")
C = [int(x) for x in C.split(",")]

U = [round(a / Au) for a in A]

print("Channels (C) : ", C)
print("Capacity (A) : ", A)
print("Users (U)    : ", U)
