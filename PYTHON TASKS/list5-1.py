from collections import Counter

n = int(input("Enter the no.of elements: "))
my_list = []
for i in range(n):
    value = int(input("Enter the values: "))
    my_list.append(value)
print(my_list)

count = Counter(my_list)
print(count)
