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
            print("not found")
        if self.root==None:
            print("tree is empty")
                           
        
                        
          
k=BinarySearchTree()
k.insertion(34)
k.insertion(35)
k.insertion(79)
k.search(89)
print(k.search(35))
k.search(78)



         

        
                    
            