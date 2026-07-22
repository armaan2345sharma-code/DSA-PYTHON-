class Node:#Making a Node class
    def __init__(self,item=None,next=None,prev=None):
        self.data=item
        self.next=next
        self.prev=prev
class dll:#Making a doubly linked list class
    def __init__(self,start=None):#Making a starting point
        self.start=start
    def is_empty(self):#Checking if the list is empty 
        return self.start is None
    def insert_start(self,data):#Inserting a node at start
        n=Node(data,self.start)
        if self.start is not None:
            self.start.prev=n
        self.start=n
    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
    def search(self,data):
        temp=self.start
        while temp is not None:
            if data==temp.data:
                return temp
            temp=temp.next
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next,temp.prev)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
            n.prev=temp 
    def delete_first(self):
        if self.start is None:
            pass
        else:
            self.start=self.start.next
            self.start.prev=None
            self.start.next.prev=None
    def delete_last(self):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            temp.prev=None
    def delete_after(self,data):
        n=self.search(data)
        if self.search is not None:
            if n == self.start:
                   self.delete_first
            else:
                temp=self.start
                while temp.next != n:
                    temp.next=n.next
                n.prev=None
                n.next.prev=temp   
    def print_list(self):#Printing the list
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next



#Driver code
l=dll()
l.insert_start(10)
l.insert_start(20)
l.insert_last(30)
l.insert_after(l.search(20),25)
l.delete_first()
l.delete_last()
l.delete_after(10)
l.print_list()