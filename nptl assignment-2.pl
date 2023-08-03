def rotatelist(l1,k):
  for i in range(0,k+1):
    a=l1.pop(0)
    l1=l1.append(a)
    return l1

l1=[1,2,3,4,5]
rotatelist(l1,1)
