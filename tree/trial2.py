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



         

        
                    
            