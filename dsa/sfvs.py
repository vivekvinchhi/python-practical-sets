
def gg(fun):
    def hifi():
        print("hifi")
        fun()
        print("done")
    return hifi
@gg
def hi():
    print("hi some is happend")
    
hi()


def ap(x,v):
    x.append(55)
    v=v+5
    
l=[45]
v = 5
ap(l,v)
print(l,v)

def fibbo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    ans = fibbo(n-1)+fibbo(n-2)
    return ans
for i in range(16):
    print(fibbo(i))
    
def saydigit(n,arr):
    if n== 0:
        return
    num = n %10
    n=n//10
    
    
    saydigit(n,arr)
    print(arr[num] , end=" ")
    
n = 456
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
saydigit(n,arr)