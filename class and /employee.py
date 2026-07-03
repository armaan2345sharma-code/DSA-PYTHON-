class employee:
    def __init__(self,name,age,salary,time):
        self.name=name
        self.age=age
        self.salary=salary
        self.time=time
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getSalary(self):
        return self.salary
    def getTime(self):
        return self.time
    def showName(self):
        print("Name:", self.name)
    def showAge(self):
        print("Age:", self.age)
    def showSalary(self):
        print("Salary:", self.salary)
    def showTime(self):
        print("Time:", self.time)
print("MOHAN")
Mohan=employee ("Johan", 30, 50000, 8)
Mohan.showName()
Mohan.showAge()
Mohan.showSalary()
Mohan.showTime()
print("KARAN")
Karan=employee("Karan",25,40000,7)
Karan.showName()
Karan.showAge()
Karan.showSalary()
Karan.showTime()