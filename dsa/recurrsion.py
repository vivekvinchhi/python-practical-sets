# def checksortted(arr,size):
#     if size == 0 or size == 1:
#         return True
#     if arr[0]>arr[1]:
#         return False
#     else:
#        return checksortted(arr[1:],size-1)
    
# def sumarr(arr,size):
#     if size==0:
#         return 0
#     if size==1:
#         return arr[0]
#     arr[0]= arr[0]+arr[1]
#     return arr[0] + sumarr(arr[2:],size-2)
   

# def findele(arr,num,size):
#     if size==0:
#         return False
#     if arr[0]==num:
#         return True
#     else:    
#         return findele(arr[1:],num,size-1)
# arr = [1,2,3,5]
# num = 32

# print(sumarr(arr,4))

# if findele(arr,num,4):
#     print("found")
# else:
#     print("not found")
    
def binarysearch(arr,key,start,end):
    if start>end:
        return False
    mid = start + (end-start)//2
    if arr[mid]==key:
        print(mid)
        return True
    elif arr[mid]>key:
        end = mid-1
        return binarysearch(arr,key,start,end)
    elif arr[mid]<key:
        start = mid+1
        return binarysearch(arr,key,start,end)
   
def checkpalindrome(i,j,s):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    
    i+=1
    j-=1
    return checkpalindrome(i,j,s)
    
def reverse(i,n,s):
    if i>=n-i-1:
        return s
    s[i],s[n-i-1] = s[n-i-1],s[i]
    i+=1
        
    return reverse(i,n,s)
        
s=list('vivek')
print(reverse(0,len(s)-1,s))
print(''.join(s))
ss='abb'
print(checkpalindrome(0,len(ss)-1,ss))
# arr = [1,2,3,4,5,6,7,8,9]
# print(binarysearch(arr,5,0,len(arr)-1))


# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
    
#     ans = fib(n-1)+fib(n-2)
#     return ans


# def prit(n):
#     if n>0:
#         n-=1
#         prit(n)
#         print(fib(n))
#     else:
#         return False
    
# prit(10)