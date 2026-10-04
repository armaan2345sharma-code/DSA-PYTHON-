def natural(n):
    if n==1:
        print("1")
    else:
        print(n)
        return natural(n-1)
y=0
def reverseNatural(o):
    if y==o:
        print(o)
    else:
        print(y)
        return reverseNatural(y+1)
t=reverseNatural(3)
k=natural(3)