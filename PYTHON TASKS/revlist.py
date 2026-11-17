n = int(input("enter how many items you want in a list: "))
mylist = []
for i in range(n):
    value = input("Enter the values: ")
    mylist.append(value)
print("original list: ",mylist)
reverse_list = mylist[: : -1]
print("reversed list: ",reverse_list)
