class node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next
class cll:
    def __init__(self, start=None):
        self.start=start
    def is_empty(self):
        return self.start is None
    def insert_start(self,data):
        n=node(data)
        if self.start is not None:
            n.next=self.start
        self.start=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
#driver code
k=cll()
k.insert_start(25)
k.print_list()
    

        
