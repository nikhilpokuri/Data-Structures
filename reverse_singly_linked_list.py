class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n:
                print(n.data,end="--->")
                n=n.ref
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def reverse(self):
        prev=None
        n=self.head
        while n:
            self.head=n
            temp=n.ref
            n.ref=prev
            prev=n
            n=temp
l=LL()
l.add_end(10)
l.add_end(20)
l.add_end(30)
l.add_end(40)
print("ORIGINAL LINKED LIST")
l.dis()
print("\n\nREVERSED LINKED LIST")
l.reverse()
l.dis()

                        #EXPLANATION
""" 
ORIGINAL==10-->>20-->>30-->>40-->>
REVERSED==40-->>30-->>20-->>10-->>

prev=None
n=10
head=n#10
temp=n.ref#20(10.ref)
n.ref=prev#None
prev=n#10
n=temp#20                               NOW LINKED LIST =10-->>

prev=10
n=20
head=n#20
temp=n.ref#30(20.ref)
n.ref=prev#10
prev=n#20
n=temp#30                               NOW LINKED LIST =20-->>10-->>

prev=20
n=30
head=n#30
temp=n.ref#40(30.ref)
n.ref=prev#20
prev=n#30
n=temp#40                               NOW LINKED LIST =30-->>20-->>10-->>

prev=30
n=40
head=n#40
temp=n.ref#None(40.ref)
n.ref=prev#30
prev=n#40
n=temp#None                         NOW LINKED LIST =40-->>30-->>20-->>10-->>
"""
