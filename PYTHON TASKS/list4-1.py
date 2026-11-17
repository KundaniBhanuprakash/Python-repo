import numpy as np

n = int(input("Enter the no.of elements: "))
my_list = []
for i in range(n):
    value = int(input("Enter the values: "))
    my_list.append(value)
print(my_list)

average = np.mean(my_list)
print("Avg of list: ", average)
