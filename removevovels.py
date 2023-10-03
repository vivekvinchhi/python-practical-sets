s = "CodingNinjas"
sl = list(s)
vovels = ['a','e','i','o','u','A','E','I','O','U']
rl = []

for i in sl:
    if i not in vovels:
      rl.append(i)  

x = ''.join(rl)
print(x)