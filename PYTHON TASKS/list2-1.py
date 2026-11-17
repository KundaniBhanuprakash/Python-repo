n = int(input("Enter the no.of elements: "))
my_list = []
for i in range(n):
    items = input("Enter the items: ")
    my_list.append(items)
print("Original list: ", my_list)
while True:
    print("Choose options: 1.Insert, 2.Delete, 3.Exit")
    choice = int(input())
    if choice == 1:
        print("choose : 1. Insert at end, 2. insert at specific pos, 3.Exit")
        choice = int(input())
        if choice ==1:
            element = input("Enter the element: ")
            my_list.append(element)
            print("After inserting list: ", my_list)
        elif choice == 2:
            pos = int(input("Enter the position: "))
            val = input("Enter the value: ")
            my_list.insert(pos, val)
            print("After insering, list: ", my_list)
        elif choice ==3:
            break
    if choice == 2:
        print("choose : 1.Delete a value, 2. delete entire list, 3. exit")
        choice = int(input())
        if choice == 1:
            value = input("Enter the deleting value: ")
            if value in my_list:
                my_list.remove(value)
                print("After deleting, list: ", my_list)
            else:
                print("Element not existed")
        elif choice == 2:
            my_list.clear()
            print("list is deleted")
            
        elif choice == 3:
            break
    if choice == 3:
        break
            
        
        
        
    
            
        
