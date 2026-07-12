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
            if temp.data==data:
                return temp
            temp=temp.next
    def insert_after(self,temp,data):
        if temp is not None:
            n=Nodes(data,temp.next)
            temp.next=n#now the previous nodes next pointing towards the n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print (temp.data,end=" " )
            temp=temp.next
    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next
    def delete_last(self):
        if self.is_empty():
            pass 
        else:
            if self.start.next is None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next is not None:
                    temp=temp.next
                    temp.next=None
    def delete_search(self,data):
        n=self.search(data)
        if n is not None:
            if n == self.start:
                self.delete_first()
            else:
                temp = self.start
                while temp.next != n:
                    temp = temp.next
                temp.next = n.next

#Driver code
myList=sll()
myList.insert_start(10)
myList.insert_start(20)
myList.insert_last(30)
myList.insert_last(40)
myList.insert_after(myList.search(20),25)
myList.delete_search(10)#delete the searched data
myList.print_list()