'''def rotatelist(l1,k):
  a=l1[k::]
  b=l1[0:k]
  c=a+b
  return (print(c))

l1=[1,2,3,4,5]
rotatelist(l1,3)
'''
x = [589,'big',397,'bash']
y = x[2:]
u = x
w = y
w = w[0:]
w[0] = 357
x[2:3] = [487]
print(x[2])
print(y[0])
print(u[2])
print(w[0])


