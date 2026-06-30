from array import *
a1= array('i',[1,67,90,87])
print(type(a1))
print("for statements")
for x in a1:
    print(x)
print("while statements")
k=0
while (k<len(a1)):
    print(a1[k])
    k+=1
print("doing append")
a1.append(39)
print(a1)
print(a1.count(0))


