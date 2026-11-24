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

    def min_item(self,temp):
        curent=temp
        while curent.left!=None:
            curent=curent.left
        return curent.data
    def BstSize(self):
        temp=len(self.postorder())
        print(temp)
    ''' def deletionP(self,data):
        temp=self.root
        tempParent=self.root
        while True:
            if tempParent.data>data:
                if tempParent.left is not None and tempParent.left.data == data:
                    break
                tempParent=tempParent.left
            if tempParent.data<data:
                if tempParent.right is not None and tempParent.right.data == data:
                    break
                tempParent=tempParent.right
        if tempParent.left.data==data:
            temp=tempParent.left
        elif tempParent.right.data==data:
            temp=tempParent.right
        if temp.left==None and temp.right==None:
            if tempParent.left==temp:
                tempParent.left=None
            elif tempParent.right==temp:
                tempParent.right=None
        if (temp.left==None and temp.right!=None)or(temp.right==None and temp.left!=None):
            tempChild=self.root
            if temp.right!=None:
               tempChild=temp.right
            elif temp.left!=None:
                tempChild=temp.left
            if tempParent.left==temp:
                tempParent.left=tempChild
            elif tempParent.right==temp:
                tempParent.right=tempChild
        if (temp.left!=None and temp.right!=None):
           
            Newtemp=temp.right
            while (Newtemp.left!=None):
                Newtemp=Newtemp.left
            NewtempParent=temp.right
            while(NewtempParent.left!=Newtemp):
                NewtempParent=NewtempParent.left
            
            if Newtemp.right==None:
                NewtempParent.left=None
            if Newtemp.right!=None:
                NewtempParent.left=Newtemp.right
                Newtemp.right=None
            
            if tempParent.left==temp:
                tempParent.left=Newtemp
                temp.right=Newtemp.right
                temp.left=Newtemp.left
            if tempParent.right==temp:
                tempParent.right=Newtemp
                temp.right=Newtemp.right
                temp.left=Newtemp.left'''
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.data:
            root.left=self.rdelete(root.left,data)
        elif data>root.data:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                root.data=self.min_item(root.right)
                self.rdelete(root.right,root.data)
            return root



                           
        
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
#k.deletionP(56)
print(k.inorder())
k.insertion(90)
k.insertion(93)
k.insertion(91)
print(k.inorder())
print(k.min_item(k.root))
k.delete(89)
print(k.inorder())
        
                    
            