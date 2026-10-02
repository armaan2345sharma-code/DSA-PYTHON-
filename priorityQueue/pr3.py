class node:
    def __init__(self,data=None,next=None,previous=None,priority=None):
        self.data=data
        self.next=next
        self.priority=priority
        self.previous=previous
class priorityQueue:
    def __init__(self,start):
        self.start=start
    def push(self,item,prior):
        temp=self.start
        n=node(item)
        n.priority=prior
        if self.start==None:
            self.start=n
            return
        if n.priority>self.start.priority:
            n.next=self.start
            self.start.previous=n
            self.start=n
            return
        

        while temp.next!=None and temp.next.priority>n.priority:
            temp=temp.next
        if temp.next==None:
            temp.next=n
            n.previous=temp
            return
                    
        n.next=temp
        n.previous=temp.previous
        temp.previous.next=n
        temp.previous=n
    def printl(self):
        temp=self.start
        while temp!=None:
            print(temp.data)
            temp=temp.next
k=priorityQueue(None)
k.push(23,4)
k.push(45,2)
k.push(89,67)
k.push(78,1)
k.printl()


        