class Counter:
    def __init__(self,start=1,end=10):
        self.start=start
        self.end=end
    def __iter__(self):
        return self.Counter_Iterator(self)
    class Counter_Iterator:
        def __init__(self,Counter):
            self.Counter=Counter
        def __next__(self):
            if self.Counter.start>self.Counter.end:
                raise StopIteration
            current_value=self.Counter.start
            self.Counter.start+=1
            return current_value
my_counter=Counter(1,5)
for i in my_counter:
    print(i)

            

