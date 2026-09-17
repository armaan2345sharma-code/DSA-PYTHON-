from sll import sll
class stacks(sll):
    def push(self,data):
        return self.insert_start(data)
    def peak(self):
        return self.start.data
    def pull(self):
        return self.delete_first
    
    def printl(self):
        return self.print_list()
k=stacks()
k.push(34)

k.push(67)
k.push(78)
k.push(90)
k.delete_first()

k.printl()
print("\nthis is peak\n",k.peak())