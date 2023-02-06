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
                print(n.pref,"|",n.data,"|",n.nref,"-->",end=" ")
                n=n.nref
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.pref is not None:
                n=n.pref
            n.pref=new_node
            self.head=new_node
            new_node.nref=n
l=Doubly_Linked_List()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)
l.display()
