class sll:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    def list_print(self):
        if self.item is None:
            return "None"
        else:
            return str(self.item) + " -> " + self.next.list_print() if self.next else str(self.item)
    def is_empty(self):
        return self.item is None
    def insert_end(self,item):
        if self.is_empty():
            self.item = item
            self.next = sll()
        else:
            self.next.insert_end(item)
    def search(self,item):
        if self.is_empty():
            return False
        elif self.item == item:
            return True
        else:
            return False
        

t3=sll(3)
t2=sll(2,t3)
t1=sll(1,t2)
t0=sll(0,t1)
print("The linked list is:")
print(t0.list_print())
print("Search for 2:", t0.search(2))