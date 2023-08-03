#Write a python program which covers all the methods (functions) of list. 

#append method

fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)

#clear method

fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)
fruits.clear()
print(fruits)

#copy list

fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)
fruits.clear()
print(fruits)
fruits=["apple","mango","grapes"]
x=fruits.copy()
print(x)

#count

fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)
fruits.clear()
print(fruits)
fruits=["apple","mango","grapes","apple","apple"]
x=fruits.copy()
print(x)
y=fruits.count("apple")
print("counts of apple in list :",y)
#append => append is used to add single element at last
#clear=> clear is used to clear entire list
#count=> count is used to count total number of element in the list
#copy=>copy is used to copy the list
#extend => add n elements at the end of list
#index => index gives index number of any value.
#insert =>inseret is used to add element at specific index
#pop=>pop is used to remove element from list
#remove=> it removes first occurence of specified value
#reverse => it revers the order of a list
#sort => it sorts the list inn alphabetical order
fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)
fruits.clear()
print(fruits)
fruits=["apple","mango","grapes","apple","apple"]
x=fruits.copy()
print(x)
y=fruits.count("apple")
print("counts of apple in list :",y)
cars=["rolls-royce","bugatti","ferrari","volvo"]
fruits.extend(cars)
print(fruits)
d=fruits.index("bugatti")
print(d)
fruits.insert(0,"shree krishna")
print(fruits)
fruits.pop(4)
print(fruits)
fruits.remove('grapes')
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.insert(0,1)
fruits.insert(1,2)
print(fruits)
'''
'''
fruits=["apple","mango","grapes"]
fruits.append("strowbarry")
print(fruits)
fruits.clear()
print(fruits)
fruits=["apple","mango","grapes","apple","apple"]
x=fruits.copy()
print(x)
y=fruits.count("apple")
print("counts of apple in list :",y)
cars=["r","b","f","v"]
fruits.extend(cars)
print(fruits)
d=fruits.index("b")
print(d)
fruits.insert(0,"A")
print(fruits)
fruits.pop(4)
print(fruits)
fruits.remove('grapes')
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.insert(0,"a")
fruits.insert(1,"b")
print(fruits)
'''
#Write a Python program to append a list to the second list. 

'''
a=["1","2","3"]
b=["4","5","6"]
a.append(b)
print(a)
'''
#Write a python program to check whether the given list is palindrome or not.
'''
a=["1","2","3","2","1"]
print(a)
b=a[::-1]
print("reversing the given list",b)
if(a==b):
    print("Entered list is palindrome")
else:
    print("enterd list is not palindrome")
'''

# Write a python program to store strings in list and then print them.
'''
s=input("Enter string :")
li=list(s.split(" "))
print(li)
'''
'''
#5 Write a python program to print list of prime numbers upto N using loop and else clause. 
a=[]
n=int(input("Enter limit of number:"))
for num in range(1,n+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            a.append(num)
print(a)
'''

#Write python program to check whether the given list is palindrome or not
#same as practical 3

#Write a Python program to multiply all the items in a list. 
'''
a=[]
n=int(input("Enter number of elements of list :"))
for i in range(1,n+1):
    x=int(input("enter element :"))
    a.append(x)
print(a)
m=1
for i in a:
    m=m*i
print("multiplication of all elements of list :",m)


'''
#Write a Python program to get the largest number from a list.
'''
a=[50,5165,45,6564,84,6846,545]
print("maximum value of list a :",max(a))
'''
#Write a Python program to find the second smallest number in a list.
'''
a=[51,54,654,3,54,5]
a.sort()
print("2nd smallest element :",a[1])
'''
#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given
#list of strings. 

'''
a=input("Enter string :")
li=list(a.split("  "))
print(li)
count=0
for i in li:
    if(len(i)>2 and i[0]==i[-1]):
        count += 1
print(count)
'''
'''
'''

#Write a Python program to remove duplicates from a list
'''
def duplicate(a):
    li=[]
    for i in a:
        if(i not in li):
            li.append(i)
    return li
print(duplicate(['1','2','3','4','2','1']))
'''
#Write a Python program to find the list of words that are longer than n
#from a given string
'''
n=int(input("Enter maximum length of word :"))
a=input("Enter string")
li=list(a.split(" "))
print(li)
s=[]
for i in li:
    if(len(i)>n):
        s.append(i)
print("String having length greater ",n," is :",s)
'''
'''
#Write a Python function that takes two lists and returns True if they have
#at least one common member. 

'''
'''
def common(x,y):
    result = False
    for i in x:
        for j in y:
            if i == j:
                result = True
                return result
    
x=input("enter element of 1st list :")
li1=list(x.split(" "))
print(li1)
y=input("enter element of 2nd list :")
li2=list(x.split(" "))
print(li2)
print(common(li1,li2))
'''
'''
#Write a Python program to print the numbers of a specified list after
#removing even numbers from it.


a=[2,23,45,68,77,12]
print("list with odd and even number :",a)
for i in a:
        if(i%2==0):
                a.remove(i)
print("list without even number :",a)
'''
'''
#Write a Python program to add two matrices. 

r=int(input("Enter number of rows :"))
c=int(input("Enter number of columns :"))

matrix=[]

print("enter entries row wise:")

for i in range(r):
        a=[]
        for i in range(c):
                a.append(int(input()))
        matrix.append(a)
for i in range(r):
        for j in range(c):
                print(matrix[i][j],end = " ")
        print()

# Program to transpose a matrix using a nested loop
'''
'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
print(len(X))
print(len(X[0]))
# iterate through rows
for i in range(len(X)):  #i=1
   # iterate through columns
   for j in range(len(X[0])):  #j=1 => r[1][1]=>x[1][1] ,r[2][1]=>x[1][2]
       result[j][i] = X[i][j]

for r in result:
   print(r)
'''
'''

x=[[3,3,3],
   [2,2,2],
   [1,1,1]]
y=[[1,2,3],
   [4,5,6],
   [7,8,9]]
r=[[0,0,0],#type of required result
   [0,0,0],
   [0,0,0]] 
print(len(x)) #length of rows
print(len(x[0])) #length of column

for i in range(len(x)):      #gives every rows
        for j in range(len(x[0])): #gives every column
                r[i][j]=x[i][j]+y[i][j]
for m in r:
        print(m)

#Flatten a nested list structure.
#Example: if list1 = [1, [2, 3], [4, 5, [6, 7] ] ] then try to convert it in 1-dimensional
#[1, 2, 3, 4, 5, 6, 7]


def removenestedlist(a):
        for i in a:
                if type(i) == list:
                        removenestedlist(i)
                else:
                        b.append(i)
        

a=[1,[2,3],[4,5,[6, 7]]]
b=[]
removenestedlist(a)
print("flatten list :",b)

#Write a Python program to split a list every Nth element.
a=[1,2,3,4,5,6,78,9,8]
b=[]
n=int(input("Enter number to split the list :"))
for i in range (0,len(a),n):
    b.append(a[i:i+n])
print(b)


















