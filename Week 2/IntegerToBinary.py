import math
integer=int(input("Input any integer number :"))

binary=  ''

while integer !=0:
    binary = binary + str(integer % 2)
    integer = int(integer /2)

print("The binary is: ",binary)


