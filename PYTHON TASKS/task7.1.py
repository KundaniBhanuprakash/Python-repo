#creating and manipulating sets

#creating set
numbers={10,20,30,40}
print(numbers)

#creating set from list
fruits=set(["apple", "banana", "mango"])
print(fruits)

#add one element
numbers.add(50)
print(numbers)

#add multiple numbers
numbers.update([60,70,80])
print(numbers)

#remove elements
numbers.remove(20)

#removing all elements
numbers.clear()
