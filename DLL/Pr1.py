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
    def print_list(self):#Printing the list
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next



#Driver code
l=dll()
l.insert_start(10)
l.insert_start(20)
l.print_list()