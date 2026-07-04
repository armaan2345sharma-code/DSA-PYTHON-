class sll:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    def list_print(self):
        if self.item is None:
            return "None"
        else:
            return str(self.item) + " -> " + self.next.list_print() if self.next else str(self.item)
t3=sll(3)
t2=sll(2,t3)
t1=sll(1,t2)
t0=sll(0,t1)
print("The linked list is:")
print(t0.list_print())
