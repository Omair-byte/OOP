import math
integer=int(input("Input any integer number :"))

binary= ""
def reverse(s):
    for i in range(len(s),0,-1):
        reverse = reverse + str (s[i-1])
    return reverse

while integer !=0:
    binary = binary + str(integer % 2)
    integer = int(integer /2)


print("The binary is: ",reverse)

