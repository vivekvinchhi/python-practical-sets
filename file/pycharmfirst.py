import random

print("vivek")
for i in range(6):
    print(i)

a = " kjksn "
print(type(a))
b = 5
print(b)
print(type(b))
c = str(b)
print(type(c))
x, y = 54, "dfv"

print(x, y, sep="#")
z = 100

print("ascci : ", chr(65))
print("random : ", random.randrange(1, 100))


def xfv():
    global z
    z = "kjdbv"
    print(z)


xfv()

print(z)
n = 5
for i in range(0, n):
    l=i
    for j in range(i+1 ):
        print(j+1, end=" ")

    for j in range(n,i,-1):
        print("*",end=" ")

    for m in range(i + 1):
        print(l+1, end=" ")
        l=l-1

    for k in range(n-1,i,-1):
        print("*",end=" ")


    print()
