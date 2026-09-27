class node:
    def __init__(self,data=None,next=None,Previous=None):
        self.data=data
        self.next=next
        self.Previous=Previous
class deque:
    def __init__(self, start=None):
            self.start = start
    def listEmpty(self):
        return self.start==None
    def addFront(self,data):
        n=node(data)
        if self.start==None:
            self.start=n
        else:
            self.start.Previous=n
            n.next=self.start
            self.start=n
    def addRear(self,data):
        temp=self.start
        n=node(data)
        while temp.next!=None:
            temp=temp.next
        temp.next=n
        n.Previous=temp
    def getFront(self):
        if self.listEmpty():
            pass
        else:
            print("the front is ",self.start.data)
    def getRear(self):
        if self.listEmpty():
            pass
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            print("the rear is",temp.data)
k=deque()
k.addFront(45)
k.addFront(67)
k.addFront(23)
k.addFront(69)
k.addRear(65)
k.getFront()
k.getRear()


            
            
    