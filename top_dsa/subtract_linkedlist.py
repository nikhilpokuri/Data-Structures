class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def dis(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n:
                print(n.data,end="")
                n=n.next
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
l1=LL()
l1.add_end(1)
l1.add_end(0)
l1.add_end(0)

l2 = LL()
l2.add_end(2)
l2.add_end(0)


def subLinkedList(l1, l2): 
    temp1 = l1
    temp2 = l2
    num1 = ''
    num2 = ''
    while temp1 and temp2:
        num1 += str(temp1.data)
        num2 += str(temp2.data)
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1:
        while temp1:
            num1 += str(temp1.data)
            temp1 = temp1.next
    if temp2:
        while temp2:
            num2 += str(temp2.data)
            temp2 = temp2.next
    new = str(abs(int(num2)-int(num1)))
    head = Node(new[0])
    temp = head
    # print(temp.data)
    for i in new[1:]:
        node = Node(i)
        temp.next = node
        temp = temp.next
    return head

res_head = subLinkedList(l1.head,l2.head) #l1.head = 100, l2.head = 20
temp = res_head
while temp:
    print(temp.data,end='')
    temp = temp.next