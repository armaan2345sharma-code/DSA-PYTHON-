class node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next
class cll:
    def __init__(self, start=None):
        self.start=start
    def is_empty(self):
        return self.start is None
    def insert_start(self,data):
        n=node(data)
        if self.start is not None:
            n.next=self.start
        self.start=n
    def insert_last(self,data):
        n=node(data)
        temp=self.start
        if temp.next is None:
            temp.next=n
            temp=temp.next
    def cll(self):
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.next=self.start
    def search(self,data):
        temp=self.start
        while True:
            if temp.data == data:
                print ("y")
                return temp
            temp=temp.next
            if temp==self.start:
                break
        return None
                
    def insert_after(self,data,key):
        temp=self.search(key)
        n=node(data)
        n.next=temp.next
        temp.next=n
    def delete_search(self,data):
        temp=lo  
            

    def print_list(self):
        if self.start is None:
            return
        temp=self.start
        while True:
            print(temp.data,end=" ")
            if temp.next is self.start:
                break
            temp=temp.next
#driver code
k=cll()
k.insert_start(25)
k.insert_last(30)
k.search(25)
k.insert_after(38,30)
k.cll()
k.print_list()
    

        
