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
    def search(self,data):
        temp=self.start
        while temp is not None and temp.data!=data:
            temp=temp.next
        return temp 
    def inserrt_after(self, data,value):
        temp=self.search(data)
        if temp==None:
            pass
        else:
             n=node(value)
             n.next=temp.next
             temp.next.prev=n
             temp.next=n
             n.prev=temp
    def delete_search(self,data):
        temp=self.search(data)
        if temp==self.start and self.start.next==self.start:
            self.start=None
        else:
            temp.prev.next=temp.next
            temp.next.prev=temp.prev

       
        


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
    def __iter__(self):
        return self.cdl_iterator(self)
    class cdl_iterator:
        def __init__(self, cdl):
            self.current = cdl.start
            self.start = cdl.start

        def __next__(self):
            if self.current is None:
                raise StopIteration

            data = self.current.data
            self.current = self.current.next

            if self.current == self.start:
                self.current = None

            return data

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
k.insert_last(90)
k.insert_last(78)
k.insert_start(98)
k.delete_last()
k.delete_start()
k.inserrt_after(10,22)
k.delete_search(22)

for i in k:
    print(i)
    

k.priint()

            




            