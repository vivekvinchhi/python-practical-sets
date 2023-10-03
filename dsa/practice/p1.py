def remove_duplicates(s):
    stack = []
    for char in s:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    return ''.join(stack)




def stringocc(s):
    arr = [0]*26
    temp = []
    for i in range(len(s)):
        char = ord(s[i])
        num = char - ord('a')
        arr[num]+=1
    
    for j in range(len(arr)):
        if arr[j]>0:
            temp.append(chr(j+ord('a'))+str(arr[j]))
            
            
    return ''.join(temp)
    

a='aaaabbbccdddee'
print(stringocc(a))        
    