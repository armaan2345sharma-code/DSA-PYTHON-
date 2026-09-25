class node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class queue:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def enque(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n
    def deque(self):
        if self.is_empty():
            pass
        else:
            self.start=self.start.next
    def getFront(self):
        if self.is_empty():
            print("the list is emoty")
        else:
            print("the front is ",self.start.data)
    def getRear(self):
        if self.is_empty():
            print("the list is emoty")
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            print("the rear is ",temp.data)

k=queue()
k.enque(56)
k.enque(90)
k.enque(68)
k.getFront()
k.getRear()




    