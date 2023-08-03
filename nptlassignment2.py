'''
def rotatelist(l1,k):
  for i in range(0,k+1):
    a=l1.pop(0)
    l1=l1.append(a)
    return l1

l1=[1,2,3,4,5]
rotatelist(l1,1)
'''

'''def mystery(l):
  if (l == []):
    return(l)
  else:
    mid = len(l)//2
    if (len(l)%2 == 0):
      return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
    else:
      return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])
  
print(mystery([22,14,19,65,82,55]))
'''

'''triples = [ (x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y > z ]

print(triples)
'''
'''
marks = {"Quizzes":{"Mahesh":[3,5,7,8],"Suresh":[9,4,8,8],"Uma":[9,9,7,6]},"Exams":{"Mahesh":[37],"Uma":[36]}}
marks["Exams"]["Suresh"].extend([44])
marks["Exams"]["Suresh"] = [44]
marks["Exams"]["Suresh"].append(44)
marks["Exams"]["Suresh"][0:] = [44]
'''

'''actor = {}
actor["Star Wars"] = ["Rey","Ridley"]
actor["Star Wars, Rey"] = "Ridley"
# actor[["Star Wars", "Rey"]] = "Ridley"
actor[("Star Wars", "Rey")] = "Ridley"
'''

a=[1,"a",2,"b","vb","jd"]
for a[-1] in a:
    print (a[-1])