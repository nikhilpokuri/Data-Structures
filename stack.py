stack=[]
def push():
    data=int(input("Enter the element:"))
    stack.append(data)
    print("\n\t\tStack is :",stack,"\n")
def pop():
    if not stack:
        print("\n\t\t\tstack is empty cannot pop\n")
    else:
        ele=stack.pop()
        print("\n\t\tRemoved element:",ele)
        print("\t\tStack is :",stack)
while True:
    print("Select a function to perform\npush\tpop\tquit")
    user=input()
    if user=="push":
        push()
    elif user=="pop":
        pop()
    elif user=="quit":
        print("\t>>Exiting program<<")
        break
    else:
        print("\n\tselect the correct function")
