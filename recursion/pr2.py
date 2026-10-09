def sumNatural(n): 
    if n==1:
        return 1
    return n+sumNatural(n-1)
print("sum of number",sumNatural(10))
def sumOdd(n):
    if n==1:
        return 1
    if n%2==0:
        n=n-1
    return n+sumOdd(n-2)
print("the sum of the odd number",sumOdd(99))
def sumEven(n):
    if n==2:
        return 2
    if n%2!=0:
        n=n-1
    return n+sumEven(n-2)
print("the sum of the even number",sumEven(99))
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print("the factorial of the numaber is",factorial(5))
def squareSum(n):
    if n==1:
        return 1
    return (n*n)+squareSum(n-1)
print("the sum of the square is ",squareSum(10))
    