string1 = input("Enter string : ")
temp = []
for i in range(len(string1)):
    x = string1[i]
    asc = ord(x)
    temp.append(asc)

temp.sort()

print("latgest ascci value : ",temp[-1])
print("smallest ascci value : ",temp[0])

def anagram():
    x = input("Enter 1st string : ")
    y = input("Enter 2nd string : ")
    if len(x)==len(y):
        p=sorted(x)
        q =sorted(y)
        if p == q:
            print("Given strings are anagram")
    else:
        print("Given string not anagarm")
        
anagram()