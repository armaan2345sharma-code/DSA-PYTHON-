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
    ''' class NotesToRvisit:'''
    

    def Transverse(self):
        level=0
        temp=self.root 
        def continuesTransverse(self,temp):
            storedNodes=[]
            while temp.right==None and temp.left!=None:
                temp=temp.left
                level=level+1
            while temp.left==None and temp.right!=None:
                temp=temp.right
                level=level+1
            if temp.left!=None and temp.right!=None:
                storedNodes.append[temp]
                temp=temp.left
                
