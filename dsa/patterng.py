# n = int(input("enter number of rows"))
n = 4
count = 10
for i in range(n+1):
    for j in range(i):
        k = count//2
        print(k,end=" ")
        k-=1

    count-=1
    print()
        