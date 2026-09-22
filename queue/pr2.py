class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enque(self,data):
        self.append(data)
    def deque(self):
        self.pop(-1)
    def getFront(self):
        if self.is_empty():
            print("nothing in object")
        else:
            print("the front is ",self[-1])
    def getRear(self):
        if self.is_empty():
            print("nothing in object")
        else:    
            print("the back is ",self[0])
    def printL(self):
        print(self)
k=Queue()
k.getFront()
k.enque(78)
k.enque(90)
k.enque(89)
k.getFront()
k.getRear()
k.printL()




    

