#tuple packing and unpacking
student=("Rahul", 20, "CSE")
name, age, branch=student
print("Name: ", name)
print("Age: ", age)
print("Branch: ",branch)

#converting a list into tuple
my_list=[10,20,30,40,50]
my_tuple=tuple(my_list)
print("List: ", my_list)
print("Tuple: ", my_tuple)
print(type(my_tuple))

#converting tuple into list
mytuple=(10,20,30,40,50)
mylist=list(mytuple)
print("Tuple: ", mytuple)
print("List: ", mylist)
print(type(mylist))
