class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doubly_Linked_list:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Doubly_Linked_list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.prev,"|",n.data,n.next,"|",end="  -->>  ")
                n=n.next
    def add_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            n.next.prev=n
    def reverse(self):
        curr=self.head
        while curr:
            self.head=curr
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
l=Doubly_Linked_list()
l.add_node(10)
l.add_node(20)
l.add_node(30)
l.add_node(40)
l.dis()
print()
print()
l.reverse()
l.dis()
