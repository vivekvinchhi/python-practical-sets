#program1
a=int(input("Enter number to check even or odd :"))
if(a%2==0):{
    print("entered number is even.")}
else:{
    print("entered number is odd.")}

#program2
a=int(input("enter number to check +ve,-ve or 0 :"))
if(a>0):
    print("enterd number is +ve.")
else:
    if(a<0):
        print("enterd number is -ve.")
    else:
        print("enterd number is zero.")

#program3
#ax^2+bx+c
print("enter value of a,b,c for ax^2+bx+c :")
a=int(input("enter value of a :"))
b=int(input("enter value of b :"))
c=int(input("enter value of c :"))
print("equation is ",a,"x^2+",b,"x+",c)
if(a==0):
    print("can not create quadratic equation:")
d=b*b-4*a*c
sqrt=d**0.5
if(d>0):
    print("roots are real and differrnt:")
    root1=(-b+sqrt)/2*a
    root2=(-b-sqrt)/2*a
    print(root1,root2)
else:
    if(d==0):
        root1=root2=-b/2*a
        print(root1,root2)
    else:
        print("root are complex")
        print((-b/2*a,"+i",sqrt/2*a))
        print(((-b/2*a),"-i",(sqrt/2*a)))

#program4 vowels and conconents

n=input("enter a single character :\n ")[0]
if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U'):
    print("enterd number is vowels")
else:
    print ("enterd number is consonent")

#program 5 maximum of three numbers

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))
if(a>b and a>c):
    print(a,"is maximum")
elif(b>a and b>c):
    print(b,"is maximum")
else:
    print(c,"is maximum")

#program 6 degree and salary


degree=input("enter your degree B.E or M.E:")
exp=int(input("enter years of experince :"))
if(degree=="B.E"):
    if(exp<5):
        print("Salary of an employee is 30000")
    else:
        print("Salary of an employee is 40000")
else:
    if(exp<5):
        print("Salary of an employee is 50000")
    else:
        print("Salary of an employee is 60000")

#program 7 check character,symbol or special character

a=input("Enter input to check it is character , nuumber or special character :")
a=ord(a)
if((a>=65 and a<=90) or (a>=97 and a<=122)):
    print("entered value is ALPHABET")
elif(a>=48 and a<=57):
    print("Enterd value is DIGIT")
else:
    print("Enterd value is SPECIAL CHARACTER")













    
                           

