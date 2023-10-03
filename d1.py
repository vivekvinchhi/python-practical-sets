# arr = [1,2,4,7,5,8]
# n = len(arr)
# # arr.sort()


# for i in range(1, n + 1):
#     if i not in arr:
#         print(i,end=" ")


# num = [1,1,2]
# num = set(num)
# num = list(num)
# print(num)

# l = [0,0,1,1,1,2,2,3,3,4]
# val = 3 
# def removeelement(arr,val):
#     j = 0
#     for i in range(len(arr)):
#         if arr[j]== val:
#             print("before",j)
#             arr.pop(j)
#             print(j)
#             print(len(arr))
#         else:
#             j+=1
#     print(arr)
#     return j

# def removeDuplicates( num):
#         i=0
#         while i <len(num):
#             for j in range(i+1,len(num)):
#                 if num[i]==num[j]:
#                     num.pop(j)
#                     break
#             else:
#                 i+=1
#         k = len(num)
#         print(num)
#         return k

# print(removeDuplicates(l))

# def rotate( num, k):
#     j=0
#     for i in range(k):
#         v=num.pop(j)
#         num.append(v)
#     print(num)             
# lm = [1,2,3,4,5,6,7]
# k = 3
# print(rotate(lm,k))
# print(max(lm))

# a=[]
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         if prices[i]<prices[j]:
#             v = prices[j]-prices[i]
#             a.append(v)
# k = max(a)
# print(k)



# def selectionshort(prices):
#     for i in range(len(prices)):
#         min = i
#         for j in range(i+1,len(prices)):
#             if prices[j]<prices[min]:
#                 min = j
#         prices[i],prices[min]=prices[min],prices[i]
#     print(prices)
        

# prices = [7,1,5,3,6,4]
# c = prices.pop()
# print(c)
# # print(selectionshort(prices))

# import module
# a = module.pr()
# print(a)

# f = open('tatvasoft.cpp',"r")
# print(f.readlines())
# f.close()

# f = open('filehandle.txt',"a")
# f.write("hi this is odoo developers")
# f.close()

# f = open("filehandle.txt","r")
# print(f.read())

# f = open("vivek.txt","w")
# f.write("vivek is a upcoming odoo developer")
# f.close()

# f = open("vivek.txt","r")
# print(f.read())

def pr(n):
    if n==0:
        return
   
    pr(n-1)
    print(n) 
        
    # if n==0:
    #     return 0
    # if n>0:
    #     print(n)
    # pr(n-1)

pr(10)
def power(i,j):
    if j ==0:
        return 1
    if j>0:
        n= i * power(i,j-1)
    
    return n
print(power(2,5))