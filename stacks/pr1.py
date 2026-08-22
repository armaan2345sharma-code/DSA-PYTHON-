class Stack:
    class Node:
        def __init__(self,data,next):
            self.data=data
            self.next=next

    def __init__(self,start):
        self.start=None
    def stack_empty(self):
        if self.start==None:
            True
        return
    def insert(self,data):
        n=Node(data)
        if stack_empty():
            self.start=n
        