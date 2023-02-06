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
                print(n.data,"|",n.ref,"    ---->    ",end=" ")
                n=n.ref
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("Linked List is empty")
        elif self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n is None:
                print("Node is not presented in linked list")
            else:
                new_node.ref=n.ref
                n.ref=new_node        
n1=Node(10)
l=LL()
l.head=n1
n2=Node(20)
n1.ref=n2
l.add_before(15,20)
l.add_before(150,20)
l.dis()
