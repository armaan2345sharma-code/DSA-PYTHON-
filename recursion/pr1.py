def natural(n):
    if n==1:
        print("1")
    else:
        print(n)
        return natural(n-1)
'''y=0
def reverseNatural(o):
    if y==o:
        print(o)
    else:
        print(y)
        return reverseNatural(y+1)
t=reverseNatural(3)'''
def oddPrint(n):
    if n==1:
        print("1")
    else: 
        while n%2==0:
            n=n-1
        print(n)
        return oddPrint(n-2)
def evenPrint(n):
    if n==0:
        print("1")
    else:
        while n%2!=0:
            n=n-1
        print(n)
        return evenPrint(n-2)
num1=1
def reverseOdd(n):
    global num1
    if num1>=n:
        print(n)
    else:
        print(num1)
        num1=num1+2
        return reverseOdd(n)
num2=0
def reverseEven(n):
    global num2
    if num2==n:
        return print(n)
    if num2>n:
        pass
    else:
        print(num2)
        num2=num2+2
        return reverseEven(n)


print("odd recursive function")
kn=oddPrint(5)
print("natural number ")
k=natural(3)
print("even number")
kj=evenPrint(7)
print("reverse even")
khj=reverseEven(8)
print("the last")
khji=reverseOdd(8)
