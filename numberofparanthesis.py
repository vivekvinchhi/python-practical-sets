s = '()((())'
balance = 0
for i in s:
    if i =='(':
        balance+=1
    elif i == ')':
        if balance>0:
            balance-=1
        else:
            balance+=1

print("Number of parenthesis required are : ",balance)
        
    