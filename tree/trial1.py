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
    

    
        
    def continuesTransverse(self):
        temp=self.root 
        level=0
        storedNodes=[]
        levelNo=[]
        while temp.right==None and temp.left!=None:
            temp=temp.left
            level=level+1
        while temp.left==None and temp.right!=None:
            temp=temp.right
            level=level+1
        if temp.left!=None and temp.right!=None:
            storedNodes.append[temp]
            levelNo.append[temp]
            temp=temp.left
        if temp.right==None and temp.left==None:
            temp=storedNodes[-1]
            storedNodes.pop[-1]
            self.continuesTransverse()
        if (temp.right==None and temp.left==None)and len(storedNodes==0):
            return
    
