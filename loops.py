
#PROGRAM to replace last n character of a string
print("PROGRAM to replace last n character of a string\n")
a=input("enter 1st string :")
b=input("enter 2nd string :")
c=int(input("enter number of character to be replaced from last : "))
p=len(a)
q=len(b)
print("length of 1st string is :-",p)
print("length of 2nd string is :-",q)
x=a[0:p-c]
y=b[0:q-c]
print("\n1st string without last" , c , "letters :-",x)
print("\n2nd string without last" , c , "letters :-",y)
f=a[p-c:]
print("\nlast two character of 1st string :-",f)
g=b[q-c:]
print("\nlast two character of 2st string :-",g)

print("\nreplacing last", c ,"character in 1st string :-",x+g)
print("\nreplacing last ", c ,"character in 2nd string :-",y+f)
print("\n---------------------------------------------------------------------------------------")

#PROGRAM to replace last 2 character of a string

print("PROGRAM to replace last two character of a string\n")
a=input("enter 1st string :")
b=input("enter 2nd string :")
ca=a[0:-2]
print("1st string without last two letters :-",ca)
da=b[0:-2]
print("\n2nd string without last two letters :-",da)
c=a[-2:]
print("\nlast two character of 1st string :-",c)
d=b[-2:]
print("\nlast two character of 2st string :-",d)

print("\nreplacing last two character in 1st string :-",ca+d)
print("\nreplacing last two character in 2nd string :-",da+c)
print("\n---------------------------------------------------------------------------------------")


#replace entered element by * except 1st element
print("\n\n\nPROGRAM to replace entered element by * except 1st element\n")
a=input("\nEnter string :-")
b=input("\nenter single character to be replaced  : ")
s=input("\nenter single character to be replaced by : ")
c=a.replace(b,s)
d=c.replace(s,b,1)
print("\nReplacing all the chasracter by ", s ,": ",c)
print("\nRepalcing all the character by " ,s, "Except 1st : ",d)
