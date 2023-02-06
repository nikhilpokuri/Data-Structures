class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n:
                print(n.data,"|",n.ref,"|",end="     --.>    ")
                n=n.ref
l=LL()             
n1=Node(10)
l.head=n1
n2=Node(20)
n1.ref=n2
l.dis()
