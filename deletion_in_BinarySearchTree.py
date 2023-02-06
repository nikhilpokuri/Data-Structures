Tree="""  INITIALLY,THE TREE LOOKS LIKE THIS 
                         10
                 6               98
           3        7 
        1
"""
print(Tree)
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key==None:
            self.key=data
        if data==self.key:
            return
        elif data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def preorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.preorder()
    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
        elif data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("\nNode is not present in Tree")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("\nNode is not present in Tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
root=BST(None)
nodes=[10,6,3,1,98,7]
for i in nodes:
    root.insert(i)
print("Before deleting:")
root.preorder()
root.delete(6)
root.delete(10)
root.delete(3)
root.delete(1)
print("\n\nAfter deleting:")
root.preorder()
