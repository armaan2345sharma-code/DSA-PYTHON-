class node:
    def __init__(self,data,next=None,prev=None):
       self.data=data
       self.next=next
       self.prev=prev
class cdl:
    def __init__(self):
        self.start=None
    def list_empty(self):
        if self.start==None:
            return True
        return False
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
    def 
    def priint(self):
        temp=self.start
        if self.list_empty():
            pass
        else:
            while True:
                temp=temp.next
                print(temp.data," ")
                if temp==self.start:
                    break
#Trial code 
k=cdl()
k.insert_start(10)
k.insert_start(20)      

k.priint()

            




            