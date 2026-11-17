#programs using list
numbers=[10,20,30,40,50]
print("Original list: ", numbers)

numbers.append(60)
print(numbers)

numbers.remove(40)
print(numbers)

numbers[0]=100
print("After update, list: ",numbers)
print("Maximum no: ", max(numbers))
print("minimum no: ", min(numbers))
print("Sum: ", sum(numbers))
