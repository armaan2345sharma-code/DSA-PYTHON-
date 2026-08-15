class node:
    def __init__(self,data,next=None,prev=None):
       self.data=data
       self.next=next
       self.prev=prev
class cdl:
    def _init_(self):
        self.start=None
    def list_empty(self):
        if self.start==None:
            return True
    def insert_start(self,data):
        n=node(data)
        if self.list_empty():
            n.next=n
            self.start=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
            self.start=n


            