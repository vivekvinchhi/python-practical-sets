n = int(input("enter number of rows"))
st = [2,3,1]
v = len(st)
l = []

for i in range(n):
    s = []
    for j in range(st[i]):
        print("enter element for ",i+1,"th row : ",end="")
        x = int(input())
        s.append(x)
    l.append(s)
print(l)

for i in range(len(l)):
    for j in range(v):
        print(l[i][j],sep=" ",end="")
    print()