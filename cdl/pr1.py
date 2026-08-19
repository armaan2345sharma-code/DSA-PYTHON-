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
    def insert_last(self,data):
        n=node(data)
        temp=self.start
        if self.list_empty():
            insert_start(n)
        else:
            while True:
                temp=temp.next
                if temp.next==self.start:
                    break
            n.next=temp.next
            temp.next.prev=n
            temp.next=n
            n.prev=temp
    def delete_last(self):
        temp=self.start
        if self.list_empty():
            pass
        else:
            if self.start.next==self.start:
                self.start=None
            else:
                while temp.next.next!=self.start:
                    temp=temp.next
                temp.next=self.start
                self.start.prev=temp
    def delete_start(self):
        if self.list_empty():
            pass
        else:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next

    def priint(self):
        temp=self.start
        if self.list_empty():
            pass
        else:
            while True:
                
                print(temp.data," ")
                temp=temp.next
                
                
                if temp==self.start:
                    break
#Trial code 
k=cdl()
k.insert_start(10)
k.insert_start(20)
k.insert_last(67)
k.delete_last()
k.delete_start()


k.priint()

            




            