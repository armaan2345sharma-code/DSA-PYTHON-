class priority_que:
    def __init__(self):
        self.item=[]
    def push(self,data,priority):
        index=0
        while index<len(self.item)and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index,(data,priority))
    def pop(self):
        if len(self.item)==0:
            return None
        else:
            return self.item.pop(0)
    def peek(self):
        if len(self.item)==0:
            return None
        else:
            print(self.item[0])
    def printl(self):
        print(self.item)
k=priority_que()
k.push(34,1)
k.push(35,1)
k.push(54,1)
k.push(43,2)
k.push(90,3)
k.push(65,2)
k.peek()
k.printl()
        