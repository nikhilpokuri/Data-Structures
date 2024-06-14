from collections import deque
def averageOfLevels(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        levelSum = 0
        for _ in range(size):
            node = queue.popleft()
            levelSum += node.key
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(levelSum/size)
    return res


#DRIVER CODE
class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.key == None:
            self.key = data
        elif self.key == data:
            return
        else:
            if data < self.key:
                if self.left:
                    self.left.add_node(data)
                else:
                    self.left = BST(data)
                
            if data > self.key:
                if self.right:
                    self.right.add_node(data)
                else:
                    self.right = BST(data)
                
    def inorder(self):
        '''
        to check the inserted nodes in the Tree
        '''
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()
            
arr = [10,3,30,2,4,20,40]
root = BST(arr[0])
for i in arr[1:]:
    root.add_node(i)
# root.inorder()
print(averageOfLevels(root))