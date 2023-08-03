
#WAP to find sum of first N numbers.

n=int(input("enter number :"))
x=n*(n+1)/2
print("Sum of 1st",n,"numbers are :",x)

#WAP to find sum of N scanned numbers.

n=int(input("Enter total numbers :"))
f=0
for i in range(n):
   i=int(input("Enter numbers :"))
   f=f+i
print("Sum of entered number is :",f)

#Write a Python program to find N!.

n=int(input("Enter number to find its factoril :"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is :",fact)


#Write a Python program to print Fibonacci series upto n terms. 

n=int(input("Enter number to find its Fibonacci series :"))
a=0
b=1
c=a+b
print(a,end=",")
print(b,end=",")
for i in range(1,n-2):
    print(c,end=",")# end removes \n from print and add ","
    a=b
    b=c
    c=a+b
print(c)


#WAP to find the reverse of given numbers (Example 2564-4652).

n=int(input("Enter number to revers it :"))

s=str(n)

s=s[::-1]

n=int(s)

print("Reversed number is ",n)




#WAP to check whether entered number is prime or not.

from math import sqrt
flag=0
n=int(input("Enter number to check prime or not :"))

if(n>1):
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        print("Entred number is not prime")
    else:
        print("Enterd number is prime")
else:
    print("Entyer number greater then 1")


#WAP to print all even numbers between 1 to n except the numbers divisible by 6.

n=int(input("enter number :"))

for i in range(n+1):
    if(i%2==0 and i%6!=0):
        print(i,end=",")

#Write a python program to check whether given number is Armstrong or not.


#153=1^3+5^3+3^3

n=int(input("Enter number check entred number is ARMSTRONG or not :"))

s=str(n)
l=len(s)
num=0
for i in s:
    num=num+int(i)**l
    
if num==int(n):
    print("Enterd number is ARMSTRONG")
else:
    print("Enterd number is not ARMSTRONG")


#Write a python program to check whether given number is Palindrome or not. 


#121=121

n=int(input("Enter number to check whether entered number is palindrome or not :"))

s=str(n)
s=s[::-1]
p=int(s)
if(p==n):
    print("entered number is palindrome")
else:
    print("enterd number is not paliondrome")


'''#WAP to print 1
              1 2
              1 2 3
              1 2 3 4
              1 2 3 4 5''' 


n=int(input("Enter number of rows of pettern :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


'''
#print *****
       ***
       **
       *'''
       
n=int(input("Enter number of rows :"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
    













