def prime(n):
    flag = 0
    for i in range(2,n):
        if n % i==0:
            return False
    return True
                    
def primeupto(n):
    l = []
    for i in range(n):
        if prime(i):
            l.append(i)
    return l

def palindrome(n):
    c = n
    s = 0
    while(n!=0):
        x = n%10
        s = s*10+x
        n = n//10
    if s == c:
        return True
    return False


def armstrong(n):
    c = n
    s = str(n)
    l = len(s)
    sum = 0
    while(n!=0):
        x = n%10
        sum = sum + pow(x,l)
        n = n//10
    print(sum)
    if sum == c:
        return True
    return False

def seiveprime(n):
    if n==0 or n==1:
        return False
    l = [True]*(n+1)
    prime=[]
    for i in range(2,n+1):
        if l[i]:
            prime.append(i)
            for j in range(2*i,n+1,i):
                l[j]=False
    return prime
                        
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    while m%n!=0:
        (m,n)=(n,m%n)            
    return n

def fibonnaci(n):
    s=0
    s1=1
    l=[s,s1]
    for i in range(n):
        s3=s+s1
        l.append(s3)
        s=s1
        s1=s3
    return l 

def findTriplets():
    # Write your code here
    # Return a list of triplets
    # n = int(input("enter number of test case : "))
    
    # l = []
    # for i in range(n):
    #     arr = []
    #     print("enter number of elements for case" ,i+1," : " ,end=" ")
    #     p = int(input())
    #     for j in range(p):
    #         print("enter element" ,j+1," of case ",i+1," : ",end=" ")
    #         x = int(input())
    #         arr.append(x)
    #     print(arr)
    arr= [79, -81, -73, 89, -3, 64, -93, 20, 29, -47]
    arr.sort()
    n=len(arr)
    target =0
    l =[]
    for i in range(n):
        lo = i+1 
        hi = n-1
        while(lo<hi):
            current = arr[i]+arr[lo]+arr[hi]
            if current==target:
                l.append([arr[i],arr[i+1],arr[i+2]])
            if  current<target:
                lo+=1
            else:
                hi-=1
    return l

print(findTriplets())
# print(seiveprime(151))
# print(gcd(9,87))  
# print(fibonnaci(15))
