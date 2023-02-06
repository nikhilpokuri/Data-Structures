class LinkedList():
    def __init__(self,data):
        self.data=data
        self.next=None
node1=LinkedList(10)
node2=LinkedList(20)
node3=LinkedList(30)
node1.next=node2
currentNode=node1
while currentNode:
    print(currentNode.data,"|",currentNode.next,"|-->",end=" ")
    if currentNode is None:
        print("none")
        break
    currentNode=currentNode.next
