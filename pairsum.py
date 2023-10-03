n = int(input("enter number of element of array : "))
target = int(input("Enter target sum : "))
l= []
for i in range(n):
    x = int(input())
    l.append(x)
temp = []
for i in range(n-2):
    if l[i]+l[i+1]+l[i+2] == target:
        x = [l[i],l[i+1],l[i+2]]
        temp.append(x)

print(temp)        
            
