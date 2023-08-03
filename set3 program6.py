#WAP to check whether entered number is prime or not.

x=int(input("enter number to check whrther enterd number is prime or not :"))
if(x%2==0 or x%3==0 or x%5==0):
    print("enterd number is not prime")
else:
    print("enterd number is prime")

#WAP to print all even numbers between 1 to n except the numbers divisible by 6.
x=int(input("entyer total number :"))
for y in range(1,x+1):    
    if(y%2==0 and y%6!=0):
       print(y)
#patter

x=int(input("enter number of lines of pettern : "))
for y in range(0,x+1,1):
    for z in range(1,y,1):
        print(z)
    print("\n")                                                        

       

