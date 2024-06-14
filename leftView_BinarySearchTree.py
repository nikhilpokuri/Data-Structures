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
            self.key==data
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
    def leftView(self,root,level,lis):
        #draft draft draft draft
        if root==None:
            return
        if level==len(lis):
            lis.append(root.data)
        self.leftView(root.lchild,level+1,lis)
        self.leftView(root.rchild,level+1,lis)
root=BST(None)
arr=[10,6,3,1,6,98,3,7]
for i in arr:
    root.insert(i)
lis=[]
root.leftView(root.lchild,0,lis)
root.leftView(root.rchild,0,lis)
print(lis)
