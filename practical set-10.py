def binarysearch(l,v):
    mid=len(l)//2
    if l[mid]==v:
        print("value found")
    elif v<l[mid]:
        return binarysearch(l[:mid],v)
    elif v>l[mid]:
        return binarysearch(l[mid+1:],v)
l=[1,2,3,4,5,6,55,56,88,99]
print(binarysearch(l,55))

def selectionsort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos = i
        (l[start],l[minpos])=(l[minpos],l[start])   
    return l


m=[45,65,62134,3434,45445,6,5,8,3,4,65,44]
print("selection short : ",selectionsort(m))  
    