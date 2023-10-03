n = 5

for i in range(1,n+1):
    count = 0
    odd = 0
    for j in range(1,n+1):
        if (i+j) % 2 ==0:
            count+=1
            print(count , end=" ")
            count-=1
        else:
            print(odd, end=" ")
    print()
    
for i in range(1,n+1):
    z=i
    for j in range(2,i+1):
        print(" ",end="")
    for k in range(n,i-1,-1):
        print(z ,end=" ")
        z+=1
    print()
for i in range(1,n):
    z=n-i
    for j in range(n,i+1,-1):
        print(" ",end="")
    for k in range(z,n+1):
        print(z , end=" ")
        z+=1
    print()
ch = ord('A')     
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch), end=" ")
    ch+=1
    print()
    
ch = ord('A') 
for i in range(1,n+2):
    for j in range( n+1,i,-1):
        print("",end=" ")
    for k in range(1,i+1):
        if k>i+2 and k<i+i:
            print(chr(ch),end=" ")
        # if i+k==i+1:
        #     print(chr(ch),end=" ")
            
        
        else:
            print(" ",end=" ")
            
    ch+=1
    print()

