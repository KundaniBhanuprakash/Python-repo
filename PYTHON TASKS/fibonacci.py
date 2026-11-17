n = int(input("Enter the no.of fibonacci terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
    
