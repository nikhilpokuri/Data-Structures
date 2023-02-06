class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("linked List is empty")
        else:
            n=self.head
            while n:
                print("|",n.data,"|",n.ref,"|",end="  ---------->>  ")
                n=n.ref
    def after_node(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print(x,"is not present in linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
n1=Node(10)
l=LL()
l.head=n1
n2=Node(20)
n1.ref=n2
l.after_node(15,10)
l.dis()
