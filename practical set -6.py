# practical-1
def isprime(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    if l==[1,n]:
        return True
    else:
        return False
# def primelist(n):
#     l=[]
#     for i in range(n+1):
#         if isprime(i):
#             l.append(i)
#     return l
n=int(input("Enter range of prime list"))
listprime=list(filter(isprime,range(n+1)))
print("list of prime number",listprime)


#-------------------------------practical-2-------------------------------------------------


# from functools import reduce
# n=int(input("entre range of number"))
# sum=reduce(lambda x,y :x+y,range(n+1))
# print(sum)

#-------------------------------practical-3-------------------------------------------------
#Write a python program to find maximum from a list using reduce.
 
# from functools import reduce
# l=[45,65,3,32,4,31,3,54]
# max=reduce(lambda x,y:x if x>y else y,l)
# print("maximum number is : ",max)

#-------------------------------practical-4-------------------------------------------------
#Write a python program to find Armstrong number in a specific range using map.

# def armstrong(n):
#     s=str(n)
#     l=len(s)
#     num=0
#     for i in s:
#         num=num+int(i)**l
#     if num==n:
#         return n
# n=int(input("Enter number to check armstrong or not"))
# print(list(filter(armstrong,map(int,range(n+1)))))
        
#-------------------------------practical-5-------------------------------------------------
# def squre(n):
#     return n**2

# def cube(n):
#     return n**3

# n=int(input("enter range :"))
# q=[squre,cube]
# for i in range(n+1):
#     print(list(map(lambda x:x(i),q)))

#-------------------------------practical-6--------------

# Write python programs using (i) map/filter and function (ii) map/filter and
# lambda (iii) list comprehension
#  Create a list to store the cube of all the elements in a given
# list.
#  Create a list of equivalent Celsius degree from Fahrenheit.
#  Create a list that stores only positive numbers from given
# list.
#  Create a list that stores only alphabets from given list. 


# def cube(n):
#     s=n**3
#     return s
# l=[1,2,3,4,5,6]
# clist=list(map(cube,l))
# print(clist)

# p=list(map(lambda x:x**3,l))
# print(p)

# q=[print(cube(i)) for i in l ]

# # ---------------------------------
# def ferenheait(c):
#     f=c*1.8+32
#     return f
# def celcius(f):
#     c=(f-32)/1.8
#     return c

# f=[59,56,23,8,3,86,4,55]
# c=[-50,56,32,42,12,3,5]

# a=list(map(ferenheait,c))
# b=list(map(celcius,f))
# print("ferenheit to celcius : ",a)
# print("celcius to ferenheit :",b)

# d=list(map(lambda x:x*1.8+32,c))
# print("ferenheit to celcius : ",d)
# e=list(map(lambda x:(x-32)/1.8,f))
# print("celcius to ferenheit : ",e)

# print("ferenheit to celcius :" )
# g=[print(ferenheait(i)) for i in c]
# print("celcius to ferenheit : ")
# h=[print(celcius(j)) for j in f]

# --------------------------------------

# def positive(n):
#     if n>0:
#         return n
# l=[-55,-65,56,-6,4,3,4]
# pos=list(filter(positive,l))
# print("Positive numbers : ",pos)

# po=list(filter(lambda x:x>0,l))
# print("Positive numbers using lambda : ",po)

# p=[print(i) for i in l if i>0]

#------------------------------------------

l=[1,2,3,"a","s","d","g","v",4,"f"]

def isalphabet(n):
    return isinstance(n,str) and n.isalpha()
             
pos=list(filter(isalphabet,l))
print("list of alphabet : ",pos)   

po=list(filter(lambda x:isinstance(x,str) and x.isalpha(),l))
print("list of alphabet using lambda : ",po)
print("list of alphabet using listcompr : ")
p=[print(i) for i in l if isinstance(i,str) and i.isalpha()]