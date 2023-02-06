class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):#inorder to perform search operation,nodes to be inserted
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
    def search(self,data):
        if self.key==data:
            print("Node is present")
        elif data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")
root=BST(None)
a=[20,4,30,4,1,5,6]
for i in a:
    root.insert(i)
root.search(20)
root.search(25)
