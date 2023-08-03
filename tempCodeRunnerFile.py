def factor(m):
    factorlist =[]
    for i in range(1,m):
        if m%i==0:
            factorlist.append(i)
    return factorlist

print(factor(16))   
        
def prime(n):
    return (factor(n)==[1,n])
        
print(prime(7))