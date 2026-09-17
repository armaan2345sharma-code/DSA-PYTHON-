class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class stack:
    def __init__(self,start):
        self.start=start
    def item_count(self):
        temp=self.start
        count=0
        while temp is not None:
            temp=temp.next
            count=count+1
    def push(self,data):
        n=node(data)
        if (self.start==None) : 
            self.start=n
        else:
            n.next=self.start
            self.start=n
    def pop(self):
        if (self.start==None) :
            pass
        else:
            self.start=self.start.next
    def print(self):
        temp=self.start
        while temp is not None:
   
            print(temp.data)
            temp=temp.next
k=stack(None)
k.push(56)
k.push(890)
k.push(60)
k.push(80)
k.print()

        