Tree="""             AFTER INSERTING NODES,THE TREE LOOKS LIKE THIS 
                                  20
                      10                        30
                  5       17               25       45
"""
print(Tree) 
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):#inorder to perform pre-order,we've to insert nodes to BST
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
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
root=BST(20)
arr=[10,30,5,17,25,45]
for i in arr:
    root.insert(i)
print("PRE ORDER")
root.preorder()        
