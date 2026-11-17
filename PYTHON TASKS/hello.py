n = int(input("enter how many items you want in a list: "))
mylist = []
for i in range(n):
    value = input("Enter the values: ")
    mylist.append(value)
print(mylist)
reverse_list = mylist[: : -1]
print(reverse_list)
