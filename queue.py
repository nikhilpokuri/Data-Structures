a=[]
def enque(data):
    #data=int(input())
    a.append(data)
    print("\t\telement enqued")
def deque():
    if a:
        a.pop(0)
        print("\t\telement dequed")
    else:
        print("  cannot deque,bcoz the queue is empty\n\t\tTRY OTHER FUNCTION")
def show():
    print(a)
while True:
    print("Select the function 'enque' or 'deque' or 'show'\n\tOR PRESS >>exit<< to close")
    d=input()
    if d=="enque":
        enque(int(input("Enter element to add:")))
    elif d=="deque":
        deque()
    elif d=="show":
        show()
    elif d=="exit":
        break
    else:
        print("select valid function")
