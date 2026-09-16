import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sll.pr1 import *
class stacks(sll):
    def push(self,data):
        return self.insert_start(data)
    def printl(self):
        return self.print_list()
k=stacks()
k.push(34)
k.printl()