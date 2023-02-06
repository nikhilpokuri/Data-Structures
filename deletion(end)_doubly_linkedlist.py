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
    def add_end(self,data):#Adding nodes to perform deletion operation
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def del_end(self):
        if self.head is None:
            print("you cannot delete empty Linked List")
        elif self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref.nref is not None:
                n=n.nref
            n.nref=None
l=Doubly_Linked_List()
l.add_end(10)
l.add_end(20)
l.add_end(30)
l.del_end()
l.display()
