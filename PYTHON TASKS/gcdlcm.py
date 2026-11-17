import math
n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = int(input("Enter the number: "))
    numbers.append(num)
hcf = numbers[0]
lcm = numbers[0]
for num in numbers[1: ]:
    hcf = math.gcd(hcf, num)
    lcm = math.lcm(lcm, num)
print("HCF: ", hcf)
print("LCM: ", lcm)
