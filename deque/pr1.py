class deque:
    def __init__(self):
        self.list=[]
    def insert_front(self,data):
        self.list.insert(0,data)
    def isnert_rear(self,data):
        self.list.append(data)
    def get_front(self):
        print("the front is",self.list[0])
    def getRear(self):
        print("the rear is",self.list[-1])
    def delete_front(self):
        self.list.pop(0)
    def printl(self):
        print(self.list)
k=deque()
k.insert_front(90)
k.insert_front(89)
k.isnert_rear(45)
k.printl()
