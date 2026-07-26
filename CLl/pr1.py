class node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next
class cll:
    def __init__(self, start=None):
        self.start=start
    def is_empty(self):
        return self.start is None
    def at_start(self):
        n=node(data,self.start)
        
