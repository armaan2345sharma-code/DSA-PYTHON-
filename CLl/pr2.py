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
            self.last=n
    def insert_last(self,data):
        n=node(data)
        if self.is_empty():
            self.last=n
            n.next=n
        else:
            n.next=self.last
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
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            if temp==self.last:
                 self.last==n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next#this is location of first node
            while temp!=None:
                print(temp.item)
                temp=temp.next
            print(temp.item)

#Experimental code
k=CLL()
k.insert_start(21)
k.insert_last(90)
k.insert_after(21,31)
k.print_list

            





                    




            

#testing code
k=CLL()
k.insert_start(45)
k.insert_last(35)