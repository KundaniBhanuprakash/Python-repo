#programs using list
numbers={10,20,30,40,50}
print("Original set: ", numbers)

numbers.add(60)
print(numbers)

numbers.remove(30)
print(numbers)

print("Is 20 present: ", 20 in numbers)

a={10,20,30,40}
b={30,40,50,60}
print("set a: ", a)
print("set b: ", b)
print("union: ", a.union(b))
print("intersection: ", a.intersection(b))
print("difference: ", a.difference(b))
