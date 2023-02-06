class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("linked list is Empty")
        else:
            n=self.head
            while n:
                print(n.data,"|",n.ref,"| ---->>",end=" ")
                n=n.ref
    def add_begin(self,data): #adding nodes,inorder to perform deletion operation
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node
    def del_end(self):
        if self.head is None:               #if there is no nodes
            print("Linked list is empty,CANNOT DELETE")
        elif self.head.ref is None:      #if there is only one Node
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
l=LL()
l.add_begin(30)
l.add_begin(30)
l.add_begin(20)
l.add_begin(10)
l.del_end()
l.del_end()
l.del_end()
l.dis()
