class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Linked List  is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"|",n.ref,"|  --->>  ",end=" ")
                n=n.ref
    def add_begin(self,data):#adding nodes,in order to perform delete operation
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def del_begin(self):
        if self.head.ref is None:
            self.head=None
        else:
            self.head=self.head.ref
l=LL()
l.add_begin(20)
l.add_begin(10)
l.dis()
l.del_begin()
l.dis()
