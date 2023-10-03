s = "kmvm"
d = 1
def rotate(strr,d):
    x = strr[d:]+strr[0:d]
    return x
def rotateright(strr,d):
    x = strr[-d:]+strr[0:-d]
    return x

print(rotate(s,d))
print(rotateright(s,d))