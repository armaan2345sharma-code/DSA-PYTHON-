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
        while n%2==0 :
            n=n-1
        print(n)
        return oddPrint(n-2)
print("odd recursive function")
kn=oddPrint(5)
print("natural number ")
k=natural(3)