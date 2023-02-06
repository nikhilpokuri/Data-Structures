class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Linked list is empty\n\tPlease add the elements to link")
        else:
            n=self.head
            while n:
                print("|",n.data,"|",n.ref,"|",end="  ---->  ")
                n=n.ref
    def add_begin(self,data):
        n=self.head
        new_node=Node(data)
        new_node.ref=n
        self.head=new_node
l=LL()
l.add_begin(5)
l.add_begin(15)
l.add_begin(25)
l.dis()
