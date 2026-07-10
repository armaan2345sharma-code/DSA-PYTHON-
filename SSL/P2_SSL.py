class Nodes:#Making of nodes
    def __init__(self, item=None, next=None):
        self.data = item
        self.next = next
class sll:#Making of linked list
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start is None
    def insert_start(self,data):
        n = Nodes(data,self.start)
        self.start = n
    def insert_last(self,data):
        n = Nodes(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
    def insert_after(self,temp,data):
        if temp is not None:
            n=Nodes(data,temp.next)
            temp.next

        return None
        