rows = int(input("enter number of rows : "))
matrix = []
colele = []

for i in range(rows):
    print("enter number of elements for ",i+1,"th row : ")
    x = int(input())
    colele.append(x)

for i in range(rows):
    s = []
    for j in range(colele[i]):
        print("enter element for ",i+1,"th row :")
        x = int(input())
        s.append(x)
    matrix.append(s)
    
print(matrix)

for i in range(rows):
    for j in range(colele[i]):
        print(matrix[i][j],end=" ")
    print()
    