#program 1
print("hellow word")
#program 2
a=1
b=2
print("before swaping :",a,b)

temp=a
a=b
b=temp
print("aftre swaping :",a,b)

#program 3
a=10
b=20
print("before swaping without using 3rd variable :",a,b)
(a,b)=(b,a)
print("after swaping without using 3rd variable :",a,b)

#program 4
a=int(input("enter number to find it's square root :" ))
x=a**0.5
print("Squarr root of ",a,"is :",x)

#program 5
length=int(input("enter length of rectangle :"))
breath=int(input("enter breath of rectangle :"))
area=length*breath
print("Area of rectangle is :",area)

radios=int(input("enter radios of circle :"))
area=3.14*radios**2
print("Area of circle is :",area)

#program 6
n=int(input("enter total number :"))
s=n*(n+1)/2
print("sum of ",n,"natural number is: ",s)

#program 7
a=int(input("enter 1st number to perform an arithmatic operations :"))
b=int(input("enter 2nd number to perform an arithmatic operations :"))
sum=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
print("sum of ",a,"and",b,"is :",sum)
print("substraction of ",a,"and",b,"is :",sub)
print("multiplication of ",a,"and",b,"is :",mul)
print("division of ",a,"and",b,"is :",div)
print("modulus of ",a,"and",b,"is :",mod)


#program 8

a=int(input("enter 1st number to perform an modulo operations :"))
b=int(input("enter 2nd number to perform an modulo operations :"))
m=a%b
print("modulo of",a,"and",b,"is :",m)
