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
            

#testing code
k=CLL()
k.insert_start(45)
k.insert_last(35)