arr = []
temp = []
n = int(input("Enter size of array : "))
for i in range(n):
    x = int(input())
    arr.append(x)
arr.sort()
print(arr)

m=0
n=len(arr)-1

while m<n:
    temp.append(arr[m])
    m+=1
    if m<n:
        temp.append(arr[m])
        m+=1
    temp.append(arr[n])
    n-=1
    if m<n:
        temp.append(arr[n])
        n-=1



print(temp)
    
    