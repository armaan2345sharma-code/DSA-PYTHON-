class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_start(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_last(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
            
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,data,temp):
        n=node(data,temp.next)
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def delete_last(self):
        temp=self.last.next
        if not temp.next==self.last:
            temp=temp.next
            self.last=temp 
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while True:
                print(temp.item)
                temp = temp.next

                if temp == self.last.next:
                    break

                
   
#Experimental code
k=CLL()
k.insert_start(21)
k.insert_start(34)
k.insert_last(90)
k.insert_after(60,k.search(90))
k.insert_last(56)
k.insert_after(100,k.search(56))
k.print_list()

            





                    




            
