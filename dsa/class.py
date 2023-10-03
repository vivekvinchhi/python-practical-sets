class abc:
    def __init__(self):
        print("vivek")

class xyz(abc):
    def __init__(self):
        # super().__init__()
        print("vinchhi")
        
def factorial(n):
    if n==0 or n==1:
        return 1
    n = n*factorial(n-1)
    return n

def gcd(m,n):
    if n>m:
        (m,n)=(n,m)
    while(m%n != 0):
        (m,n)=(n,m%n)
    return n
def sqrt(n,g=1):
    x0 = g
    while True:
        x1 = (x0+n/x0)/2
        if x1 == x0:
            return x1
        x0 = x1


print(gcd(15,30))
print(factorial(5))
print(sqrt(25))