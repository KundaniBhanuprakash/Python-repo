mylist = [4, 55, 66, 4, 6, 9, 10, 55]
print("Original list: ", mylist)
unique_data = list(dict.fromkeys(mylist))
print("After removing duplicate items, list: ", unique_data)
