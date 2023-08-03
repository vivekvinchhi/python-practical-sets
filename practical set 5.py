#program 1

# initialize the set directly 

a=({})
print("initialize the set directly :- ",a)
# initialize empty set and then add values
a=set()
a.add(5)
print(" initialize empty set and then add values :-",a)
# from a list 

x=[1,2,3,4,5]
z=set()
z.update(x)
print(" from a list :-",z)
# from another set
a={9,8,7,6,5}
b=set()
b.update(a)
print(" from another set :-",b)
# using range
a=set(range(0 , 9))
print(" using range :- ",a)
# update an existing set using another set
b={"vivek","one","two"}
b.update(a)
print(" update an existing set using another set :- ",b)
# print the elements of set iteratively
print(" print the elements of set iteratively :-")
for i in b:
    print(i) #it will print all the value unorderdly
# check the functionality of remove and discard
b.remove("one")
print("after removing 'one' from set b :-",b) #it will generate an error if 'one' is not present in the set
#discard
b.discard("two")
print("after discarding 'two' from set b :-",b) #it will not generate an error if 'two' is not present in the set

#program 2

x={8,9,11,12,13,14,15,16,55}
a={11,12,13,14,15,16}
b={11,55,13,16,8,9}
c=a-b
print("difference of two set is :- ",c)
c=a.intersection(b)
print("intersection of two set is :- ",c)
c=a.union(b)
print("union of two set is :- ",c)
c=a.symmetric_difference(b)
print("symmetric_difference of two set is :- ",c)
c=b.issubset(x)
print("b is subset of x :- ",c)
c=x.issuperset(a)
print("x is superset of b :- ",c)

#program 3

def find_dups(lst):
    b=set()
    for i in set(lst):
        if(a.count(i)>1):
            b.add(i)
    return b
a=[1,1,1,2,3,4,6,8,95,6,6,6]
print(find_dups(a))


#program 4

p=int(input("enter totla no. of customers :"))
for i in range(0,p+1):
    a=int(input("enter customers acc no. : "))
    b=str(input("enter name of a customer : "))
    c=int(input("enter purchased product no : "))
    d=str(input("enter product category 'bread','butter' or 'milk' "))
    e=int(input("enter unit price : "))
    x=[]
    x.insert(a,b)
    x.insert(c,d)
    x.append(e)
    print(x)
    y=set()
    y.update(x)
    g=x.count('bread')
print(x)
print(y)
print(g)
    

#program 5

a=()
print(type(a))
x= ("a",)
print("touple with single value : ",type(x),x)
y=("vivek","vinchhi","only","one",)
z=("vivek","vinchhi",1,"star",11,12.5)
for i in z:
    print(i," :data type: ",type(i))


#program 6


x=("vivek",1,"star","fighter",11.1,"fighter")
y=(1,2,32,154,613,2135,435,321,54)
#len() function finds length of an tuple 
print("Length of tuple : ",len(x))
#max() function finds maximum value from a tuple it suppors only on "int" type tuple
print("maximum of tuple : ",max(y))
#min() is used to find minimum value of a tuple
print("minimum of tuple : ",min(y))
#index() is used to find index of a value if not present returns error
print("index of fighter : ",x.index("fighter"))
#count is used to count number of times items exists in tuple
print("count of fighter : ",x.count("fighter"))



#program 7


def find(tup,*items):
    y=[]
    for i in items:
        if i in tup:
            y.append(i)
    return y
            
x=("vivek",1,"star","fighter",11.1,"fighter")
print(find(x,"vivek","star","equal"))



#program 8

x={"1a":11,"2b":22,"3c":23,"4d":55,"5e":66}
print(x.keys())
x["6f"]=77
print(x.keys())



#program 9

d=dict()
for i in range(1,16):
    d[i]=i**2
print(d)


#program 10

x={"1a":11,"2b":22,"3c":23,"4d":55,"5e":66}
y=input("enter key :")
if y in x:
    print("Entered key already eists in dictionary")



#program 11

x={"1a":11,"2b":22,"3c":23,"4d":55,"5e":66}
y={"1a1":111,"2b2":222,"3c3":233,"4d4":554,"5e5":665}

def merge(x,y):
    return(x.update(y))

print("meargeing x and y dictionary :",merge(x,y))
print(x)



#program 12


x={"1a":11,"2b":22,"3c":23,"4d":55,"5e":66}
print("before removing 1st key",x)
x.pop("1a")
print("after removing 1st key",x)


#program 13


def create_dict(list1,list2):
    d=dict()
    for i in list1:
        for j in list2:
            d[i]=j
            list2.remove(j)
            break
    return(d)

l1=[1,2,3,45,6,8]
l2=[45,55,66,88,99,22]
print(create_dict(l1,l2))



#program 14

def empty(a,b,c):
    list1=[a,b,c]
    if len(a)==0:
        print("1st dictionary is empty")
    elif len(b)==0:
        print("2nd dictionary is empty")
    elif len(c)==0:
        print("3rd dictionary is empty")
    else:
        print("none of dictionary is empty")
    
    
    

x={"1a":11,"2b":22,"3c":23,"4d":55,"5e":66}
y={}
z={"1a1":111,"2b2":222}
empty(x,y,z)


