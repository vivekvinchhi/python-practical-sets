'''
def rotatelist(l1,k):
  for i in range(0,k+1):
    a=l1.pop(0)
    l1=l1.append(a)
    return l1

l1=[1,2,3,4,5]
rotatelist(l1,1)
'''

def mystery(l):
  if (l == []):
    return(l)
  else:
    mid = len(l)//2
    if (len(l)%2 == 0):
      return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
    else:
      return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])