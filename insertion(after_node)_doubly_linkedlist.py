class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref
    def add_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,x,data):
        new_node=Node(data)
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Node is not present in Linked List")
            else:
                new_node.pref=n
                new_node.nref=n.nref
                n.nref=new_node
                if n.nref is not None:
                    n.nref.pref=new_node
l=Doubly_Linked_List()
l.add_node(10)
l.add_node(20)
l.add_node(30)
l.add_after(10,200)
l.display()
                
