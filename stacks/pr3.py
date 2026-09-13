class stack(list):
    def push(self,data):
        self.append(data)
    def is_empty(self):
        return len(self)==0
    def pop(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        else:
            return  super().pop()
    def peak(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        else:
            return self.item[-1]
    def printL(self):
        print(list(self))
f=stack()
f.push(3)
f.push(6)
f.push(7)
f.push(90)
f.push(345)
f.printL()

