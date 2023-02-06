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
                print("|",n.data,"|",n.ref,"|",end="  ---->  ")
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
l=LL()
l.add_end(40)
l.add_end(400)
l.add_end(1000)
l.dis()
