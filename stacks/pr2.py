class stacks:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def printL(self):
        print(self.items)
k=stacks()
k.push(45)
k.push(56)
k.push(56)
k.push(90)
k.printL()
