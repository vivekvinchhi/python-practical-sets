# def root(n):
#     x=[]
#     for i in range(1,n+1):
#         if(n%i==0):
#             x.append(i)
#     return x

# def primeno(n):
#     return root(n)==[1,n]

# def primeupto(m):
#     l=[]
#     for i in range(1,m+1):
#         if primeno(i):
#             l.append(i)
#     return l

# print(primeupto(200))

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
        
# print(factorial(5))

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
print(result)

            