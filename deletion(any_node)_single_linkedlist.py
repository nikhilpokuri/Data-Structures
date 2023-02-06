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
    def delete_node(self,x):
        if self.head is None:
            print("Cannot delete empty Linked List")
        elif x==self.head.data:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                else:
                    n=n.ref
            if n.ref is None:
                print("Node is not present in Linked List")
            else:
                n.ref=n.ref.ref
l=LL()
l.add_end(10)
l.add_end(20)
l.add_end(30)
l.add_end(40)
l.delete_node(40)
l.delete_node(10)
l.dis()
