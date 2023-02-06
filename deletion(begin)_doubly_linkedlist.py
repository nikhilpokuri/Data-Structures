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
                print(n.pref,"|",n.data,"|",n.nref,"|",end="---->")
                n=n.nref
    def add_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            new_node.pref=n
            n.nref=new_node
    def del_begin(self):
        if self.head is None:
            print("you cannot delete empty Linked List")
        elif self.head.nref is None:
            self.head=None
        else:
            if self.head.pref is None:
                self.head.nref.pref=self.head.pref
                self.head=self.head.nref
l=Doubly_Linked_List()
l.add_node(10)
l.add_node(20)
l.add_node(30)
l.add_node(40)
l.del_begin()
l.del_begin()
l.display()
