class Test:
    T1=5#class object variable= static variable
    print("hello")
    def f1(self):#this is instance method is called by instance object of class
        print("this is instance method")
    def __init__(self,a,b):#this is constructor method which calls automatic when we create instance object of class
        print("this is constructor method")
        self.a=a
        self.b=b
        print(a,b)
        
    @classmethod
    def f2(cls):#this is class method is called by class name
        print("this is class method ")
    @staticmethod
    def f3():#this is static method 
        print("this is static method ")

t1=Test(10,20)#instance object of class Test
 
t1.f1()#calling method f1() on instance object t1
Test.f2()#calling class method f2() on class name
Test.f3()#calling static method f3() on class name