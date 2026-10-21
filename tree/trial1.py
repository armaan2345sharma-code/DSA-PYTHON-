class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.right=right
        self.data=data
class Tree:
    def __init__(self,root):
        self.root=root
    def RootNode(self,data,left=None,right=None):
        n=Node(left,data,right)
        self.root=n