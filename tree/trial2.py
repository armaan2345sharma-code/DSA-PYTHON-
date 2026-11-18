class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.data=data
        self.right=right
class BinarySearchTree:
    def __init__(self,root=None):
        self.root=root
    def insertion(self,dat):
        n=Node(data=dat)
        if self.root==None:
            self.root=n
        else:
            temp=self.root
            while True:
                if n.data>temp.data:
                    if temp.right==None:
                        temp.right=n
                        break
                    temp=temp.right
                    
                else:
                    if temp.left==None:
                        temp.left=n
                        break
                    temp=temp.left
                    
    def search(self,dataa):
        temp=self.root
        while temp is not None:
            if temp.data==dataa:
                return temp.data
            
            if temp.data>dataa:
                temp=temp.left
            
            elif temp.data<dataa:
                temp=temp.right
        if temp==None:
            
            if self.root==None:
                print("tree is empty")
            else:
                print("not found")
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result 
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.data)
            self.rinorder(root.right,result)
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.data)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.data)
    def minimumItemnode(self):
        temp=self.postorder()
        print(temp[-1])
    def maximumItemnode(self):
        temp=self.postorder()
        print(temp[1]) 
    def BstSize(self):
        temp=len(self.postorder())
        print(temp)
    def deletionP(self,data):
        temp=self.root
        tempParent=self.root
        while True:
            if tempParent.data>data:
                if tempParent.right.data==data or tempParent.left.data==data:
                    break
                tempParent=tempParent.left
            if tempParent.data<data:
                if tempParent.right==data or tempParent.left==data:
                    break
                tempParent=tempParent.right
        if tempParent.left.data==data:
            temp=tempParent.left
        elif tempParent.right.data==data:
            temp=tempParent.right
        if temp.left=='/0' and temp.right=='/0':
            if tempParent.left==temp:
                tempParent.left=None
            elif tempParent.right==temp:
                tempParent.right=None
        if (temp.left=='/0'and temp.right!='/0')or(temp.right=='/0'and temp.left!='/0'):
            tempChild=self.root
            if temp.right!='/0':
               tempChild=temp.right
            elif temp.left!='/0':
                tempChild=temp.left
            if tempParent.left==temp:
                tempParent.left=tempChild
            elif tempParent.right==temp:
                tempParent.right=tempChild
            

    
    
                           
        
k=BinarySearchTree()
k.insertion(34)
k.insertion(35)
k.insertion(79)
k.search(89)
print(k.search(35))
k.search(78)
k.insertion(56)
k.insertion(89)
k.insertion(92)
print(k.postorder())
print(k.preorder())
print(k.inorder())
k.minimumItemnode()
k.maximumItemnode()
k.BstSize()
k.deletionP(56)
print(k.inorder())
         

        
                    
            