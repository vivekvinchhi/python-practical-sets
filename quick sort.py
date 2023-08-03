# def quicksort(l,p,q):
#     if q-p<=1:
#         return()
        
#     yellow=p+1
#     for green in range(p+1,q):
#         if l[green]<=l[p]:
#             l[yellow],l[green]=l[green],l[yellow]
#             yellow=yellow+1
    
#     l[p],l[yellow-1]=l[yellow-1],l[p]
#     quicksort(l,p,yellow-1)
#     quicksort(l,yellow,q)
    
# l=[45,654,21,4,68,321,354,332,134,356,4,6,8,35]
# quicksort(l,0,len(l))
# print(l)
# def ex():
#     b=int(input("jdc"))
#     try:
#         if b<1:
#             raise ValueError("entrer number greater then 0")
#     except ValueError as e:
#           return e
#     else:
#         print("you are a king")
#     finally:
#         print("chbvj")
# print(ex())
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "color"
  
# }
# thisdict["color"].append("s")
# print(thisdict)   

# g=open('C:\\Users\\vinch\\Downloads\\ddd.txt','r')
# h=open('C:\\Users\\vinch\\Downloads\\dd.txt','w')
# for line in g.readlines():
#   h.write(line)

# s="c aa aba"
# x=s.find("a",0,len(s))
# print(x)
# y=s.replace("a","b",2)
# print(y)
# print(s.split())

# def f():

#     def l(a):
#         return (a+1) 
#     def n(b):
#         return (b*2)
#     def m():
#         global x
#         y=l(x)+n(x)
#         print(y)
#         x=22
#     m()
# x=7
# f()

# class point():
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def tran(self,del0,del1):
#         self.x+=del0
#         self.y+=del1
#     def getself(self):
#         return(self.x,self.y)
    
# a=int(input("enter number :"))
# b=int(input("enter number :"))
# p=point(a,b)
# p.tran(22,2)
# print(p.getself())

# class node():
#     def __init__(self,intval =None):
#         self.value=intval
#         self.next=None
#     def isempy(self):
#         return(self.value==None)
    
# l=node(5)
# print(l.isempy())
      
# l={}
# print(type(l))
# l=()
# print(type(l))

# a=[1,2,3]
# for a[-2] in a:
#     print(a[-2],end='')
# b=(1,2,3,[5,6,7])
# b[3][1]=0
# print(b)
# c='vivek'
# print(c.capitalize())


# def mystery(l):
#   l = l[2:]
#   return(l)

# mylist = [7,11,13,17,19,21]
# print(mystery(mylist))
# h=[1,2,3,4,5,6]
# i=h[:4]
# h.insert(5,566)
# print(h)
# x=h
# h[2]=10
# print(x)
# print(i)
# p="vivek vinchhi"
# print(p.split(","))

# print(6&3)

# s={1,2,3}
# p={55,66,33,22}
# print(s.update(p))
# print(s)
# # thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# # print(thistuple[1])

# d=5
# e=6
# print(compare(d,e))

# def g():
#     global l,v
#     a=l+[2]
#     b=a+[3]
#     x=v+21
#     y=v+56
#     print(a)
#     print(b)
#     print(x)
#     print(y)

# l=[15]
# v=10
# g()
# t=int(input())
# while t>0:
#     x,h=[int(i) for i in input().split()]
#     if x>=h:
#         print("YES")
#     else:
#         print("NO")
#     t=t-1
# x,h=[int(i) for i in input().split()]
# t=int(input())
# while t>0:
#     n=int(input())
#     if n%3==0:
#         print("YES")
#     else:
#         print("NO")
#     t=t-1

# t=int(input())
# for i in range(t):
#     n,m=[int(i) for i in input().split]
#     y=n*m
#     print(y)

# t = int(input("enter no of turn :",))
# for i in range(t):
#     m=int(input("enter size of array :",))
#     p=0
#     for j in range(m):
#         p=p+[int(j) for j in input().split()]
#     print(p)
#     # cout=0
#     # for i in len(x):
#     #     for j in len(x):
#     #         if x[i]==x[j]:
#     #             cout=cout+1
            
    # t=t-1
    
# t = int(input())
# for i in range(t):
#     n=int(input())
#     a=list(map(int,input().split()))
#     print(a)

# n = int(input("Enter the size of the array: "))

# # Ask the user to enter the elements of the array separated by spaces
# # and check that the number of elements entered matches the desired size
# while True:
#     user_input = input(f"Enter {n} elements of the array separated by spaces: ")
#     input_list = user_input.split()
#     if len(input_list) == n:
#         break
#     print(f"You entered {len(input_list)} elements. Please enter {n} elements.")

# # Convert the list of strings into a list of integers using map() and int()
# array = list(map(int, input_list))

# # Print the resulting array
# print("The resulting array is:", array)

# t = int(input())
# for i in range(t):
#     f=int(input())
#     vf=input().split()
#     a=list(map(int,vf))
#     for i in range(a):
#        if a[i] in a:
#            x=a.find(a[i],i,a)
#     while x>1:
#         a.remove(a[i])
#         x=x-1
            
               
#     print(a)

# l=[5,7,1,2,8,4,3]
# x=int(input("enter number",))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==x:
#             print("True")
#             break
#         break
#     else:
#         continue
#     break
# else:
#     print("False")

# t = int(input())
# while t>0:
#     n=int(input())
#     x=list(map(int,input().split()))
#     x.sort()
#     t=t-1n

t= int(input())
while t>0:
    x,y=[int(i) for i in input().split()]
    if x+y>6:
        print("YES")
    else:
        print("NO")
    t=t-1