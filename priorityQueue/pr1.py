class prioriyQueue:
    def __init__(self):
        self.listP1=[]
        self.listP2=[]
        self.listP3=[]
        self.List=[]

    def push(self,prority,data):
        if prority==1:
            self.listP1.insert(0,data)
        if prority==2:
            self.listP2.insert(0,data)
        if prority==3:
            self.listP3.insert(0,data)
        self.List=self.listP1+self.listP2+self.listP3
    def pop(self):
        self.List.pop(0)

        
    
    def printl(self):
        print(self.List)
k=prioriyQueue()
k.push(1,34)
k.push(1,35)
k.push(1,54)
k.push(2,43)
k.push(3,90)
k.push(2,65)
k.pop()
k.printl()
        