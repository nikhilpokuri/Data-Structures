rootTree="""  INITIALLY,THE TREE LOOKS LIKE THIS 
                         10
                6               98
           3        7 
        1
"""
print(rootTree)
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):#inorder to perform in-order,we've to insert nodes to BST
        if self.key is None:
            self.key=data
        elif self.key==data:
            return
        else:
            if data<self.key:
                if self.lchild:
                    self.lchild.insert(data)
                else:
                    self.lchild=BST(data)
            else:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild=BST(data)
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
root=BST(10)
arr=[6,3,1,6,98,3,7]
for i in arr:
    root.insert(i)
print("INORDER TRAVERSAL")
root.inorder()

