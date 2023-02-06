class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
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
root=BST(None)
a=[20,4,30]
for i in a:
    root.insert(i)
print("\t",root.key)
print(root.lchild.key,"\t\t",root.rchild.key)
