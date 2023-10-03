matrix = []
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

for i in range(rows):
    y=[]
    for j in range(cols):
        x = int(input())
        y.append(x)
    matrix.append(y)
print(matrix)
for k in matrix:
    print(k)
    
srow = 0
scol = 0
erow = rows - 1 
ecol = cols - 1
count = 0 
total = rows*cols
ans = []

while count < total:
    # first row
    for i in range(scol,ecol+1):
        ans.append(matrix[srow][i])
        count+=1
    srow+=1
    # last col
    for i in range(srow,erow+1) :
        ans.append(matrix[i][ecol])
        count+=1
    ecol-=1
    
    # last row
    if srow<=erow:
        for i in range(ecol,scol-1,-1) :
            ans.append(matrix[erow][i])
            count+=1
        erow-=1
    # first col
    if scol<=ecol:
        for i in range(erow,srow-1,-1) :
            ans.append(matrix[i][scol])
            count+=1
        scol+=1
    
    
print (ans)

rotate = []
srow = 0
scol = 0
erow = rows - 1 
ecol = cols - 1
while scol<=ecol:
    d=[]
    for i in range(erow,srow-1,-1):
        d.append(matrix[i][scol])
    scol+=1
    rotate.append(d)

print(rotate)

for o in range(len(rotate)):
    for p in range(cols):
        print(rotate[o][p],end=" ")
    print()
