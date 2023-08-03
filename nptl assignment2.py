# # # '''
# # # def rotatelist(l1,k):
# # #   for i in range(0,k+1):
# # #     a=l1.pop(0)
# # #     l1=l1.append(a)
# # #     return l1

# # # l1=[1,2,3,4,5]
# # # rotatelist(l1,1)
# # # '''

# # # # def mystery(l):
# # # #   if (l == []):
# # # #     return(l)
# # # #   else:
# # # #     mid = len(l)//2
# # # #     if (len(l)%2 == 0):
# # # #       return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
# # # #     else:
# # # #       return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])
  
  
# # # # def fact(n):
# # # #     if n<=0:
# # # #         return 1
# # # #     else:
# # # #         x=n*fact(n-1)
# # # #         return x
# # # # print(fact(5))
    


# # # # def gcd(m,n):
# # # #     if m<n:
# # # #         (m,n)=(n,m)
# # # #     while m%n:
# # # #         (m,n)=(n,m%n)
# # # #     return n
# # # # print(gcd(25,15))

# # # # print(25%15)




# # # # def power(m,n):
# # # #     a=1
# # # #     for i in range(0,n):
# # # #         a=a*m
# # # #     return (a)
# # # # print(power(3,3))


# # # # def update(x,y,z):
# # # #     if y>=0 and y<len(x):
# # # #         x[y]=z
        
    
# # # # l=[55,66,5,3,565,53]
# # # # print(update(l,2,55666))


# def factor(m):
#     factorlist =[]
#     for i in range(1,m):
#         if m%i==0:
#             factorlist.append(i)
#     return factorlist

# print(factor(5))   
        
# def prime(n):
#     return (factor(n)==[1,n])
        
# print(prime(5))

# # # def primeupto(p):
# # #     l=[]
# # #     for i in range(p+1):
# # #         if prime(i):
# # #             l=l+[i]
# # #     return l

# # # print(primeupto(5))

        
        
# # def f(x):
# #     d=0
# #     y=1
# #     while y <= x:
# #         d=d+1
# #         y=y*3
# #     return(d)
# # print(f(2343))


# # def f(a, L=[]):
# #     L.append(a)
# #     return L


# # print(f(2))

# # def selectionsort(l):
    
# #     for start in range(len(l)):
# #         minpos = start
# #         for i in range(start,len(l)):
# #             if l[i]< l[minpos]:
# #                 minpos = i
# #         (l[start],l[minpos])=(l[minpos],l[start])
    
        
# # l=[4,6,8423,1,56,8,3,21,564,32,4]
# # selectionsort(l)
# # print(l)

# def binarysearch(seq,v,f,l):
#     if (f-l == 0):
#         return(False)
#     mid = (f+l)//2
    
#     if(v==seq[mid]):
#         return(True)
#     elif (v<seq[mid]):
#         return(binarysearch(seq,v,f,mid))
#     elif (v>seq[mid]):
#         return(binarysearch(seq,v,mid+1,l))
    
            
# seq=[1,2,3,4,5,6,7,9]

# a=binarysearch(seq,8,0,len(seq))
# print(a)


# # def suml(l):
# #     if l==[]:
# #         return (0)
# #     else:
# #         return(l[0]+suml(l[1:]))
# # l=[4,564,4,8543,84,6,89,76,5,6654,68,96]
# # print(suml(l))


# def matrlh(l):
#     b=[]
#     for i in l:
#         c=i[::-1]
#         b.append(c)
#     return (b)

# def matrlv(l):
#     b=l[::-1]
#     return(b)

# def matrixflip(l,d):
#     if d =='h':
#         return(matrlh(l))
#     elif d=='v':
#         return(matrlv(l))
    
    
# def splitsum(l):
#     p=0
#     n=0
#     for i in l:
#         if i>0:
#             p=p+i**2
#         elif i<0:
#             n=n+i**3
#     return([p,n]) 

# def remdup(l):
#     if len(l)<=1:
#         return(l)
#     if l[0] in l[1:]:
#         return(remdup(l[1:]))
#     else:
#         return([l[0]]+remdup(l[1:]))

# print(remdup([3,5,7,5,3,7,10]))

# print(	
# splitsum([1,4,-9,16,-25,36,-49,64]))   
    
    
        
    

# l=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrixflip([[1,2,3],[4,5,6],[7,8,9]],'h'))



# l=[88,99,5,6,2,3,333]
# mid =len(l)//2
# print(mid)

# print(l[mid:mid+1])



# def mergesort(a,b):
#     (c,m,n)=([],len(a),len(b))
#     (i,j)=(0,0)
#     while (i+j<m+n):
        
#         if i==m:
#             c.append(b[j])
#             j=j+1
#         elif j==n or a[i]<=b[j]:
#             c.append(a[i])
#             i=i+1
#         elif a[i]<=b[j]:
#             c.append(a[i])
#             i=i+1
#         elif a[i]>b[j]:
#             c.append(b[j])
#             j=j+1
#     return(c)


# a=list(range(15,2000))
# b=list(range(0,20))

# print(mergesort(a,b))
# f=15e7
# c=15j
# print(type(f))
# print(type(c))
# # c=int(c)
# # print(type(c))
# a = "Hello, World! "
# print(a.strip())
# b="hello"
# print(b*3)
# l=[4,6,65,6,53,5,"12165"]
# for i in l:
#     print(i)
# print(l)
# print(l[6])
# thistuple = ("1",'1'+'1')
# print(type(thistuple[1]))
# print(thistuple[1])

# class one():
#     ss=15
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def two(self):
#         print(x,y)
# p1=one(30,50)
# print(p1.x,p1.y,p1.ss)

# def isprime(n):
#     l=[]
#     for i in range(1,n+1):
#         if(n%i==0):
#             l.append(i)
#     if l==[1,n]:
#         return True
#     else:
#         return False
    
# n=20
# x=list(filter(isprime,range(n+1)))
# print(isprime(20))

# from functools import reduce
# l=[45,556,58,64,54,54,33,5]
# mape=reduce(lambda x,y: x if x>y else y,l)
# print(mape)

# def square(n):
#     return n**2
#     print(x)
# def cube(m):
#     return m**3
   
# q=[square,cube] 
# p=int(input())
# for i in range(p+1):
#     print(list(map(lambda x: x(i),q)))
# print(l)
# from functools import reduce
# l=[55,6,3,8,5,68,65,6,5,33,53]
# print(list(filter(lambda x : x>18,l)))  
# print(list(map(cube,l))) 
# print(reduce(lambda x,y : x if x>y else y, l))


# n=20
# print(reduce(lambda x,y:x+y,range(n+1)))

# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
   
# print(fact(5))

# def armstrong(n):
#     s=str(n)
#     l=len(s)
#     p=0
#     for i in s:
#         p=p+int(i)**l
#     if p==int(n):
#         print("number is armstrong")
#     else:
#         print("not")
# print(armstrong(152))

# s={4,56,54,35,3135,64,545}
# print(s)
# print(s.pop())

# l=[45,565,88,56]
# m=l[::-1]
# print(l)
# print(m)
# x=-1
# if x > 0:
#     pass 
#     print(x)
# else:
#     pass
n=int(input("Enter number of rows"))
i=1
while (i<=n):
    j=1
    while(j<=n):
        print(j)
    print("\n")
    


















