stack = []

def push():
    element = int(input("Enter the elemet: "))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("popped element is: ",e)
        print(stack)

while True:
    print("choose options: 1. push, 2. pop, 3. exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct option: ")
                 
