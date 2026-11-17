#creating array
arr=[10,20,30,40]
print("array: ", arr)
print(type(arr))

#traverse an array
arr=[10,20,30,40]
for i in arr:
    print(i)

#insertion deletion updates
arr=[10,20,30,40]
arr.insert(2, 25)
print("After insertion: ", arr)

arr.remove(30)
print("After deletion: ",arr)

arr[2]=100
print("After update: ", arr)

#max min sum avg
arr=[37,95,99,88,56]
print("Maximum no: ", max(arr))
print("Minimum no: ", min(arr))
print("sum: ", sum(arr))
print("Averege: ", sum(arr)/len(arr))
