#union
a={10,20,30,40,50}
b={30,40,50,60,70}
result=a.union(b)
print("Union: ", result)

#intersection
a={10,20,30,40,50}
b={30,40,50,60,70}
result=a.intersection(b)
print("Intersection: ", result)

#difference
a={10,20,30,40,50}
b={30,40,50,60,70}
result1=a.difference(b)
result2=b.difference(a)
print("a-b: ", result1)
print("b-a: ", result2)
