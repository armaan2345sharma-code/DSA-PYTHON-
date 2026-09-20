class queue:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def enque(self,data):
        self.list.append(data)
    def deque(self):
        self.list.pop(0)
    def getFront(self):
        print("the oldest enterd is ",self.list[0])
    def getRear(self):
        print("the latest enterd is ",self.list[-1])
    
    def printL(self):
        print(self.list)
k=queue()
k.enque(34)
k.enque(90)
k.enque(87)
k.enque(36)
k.enque(88)
k.getFront()
k.deque()
k.getRear()
k.printL()