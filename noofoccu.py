# def occ(string):
#     arr = [0]*26
#     temp = []
#     for i in s:
#         c = ord(i)
#         x = c - ord('a')
#         arr[x]+=1
    
#     for i in range(26):
#         if arr[i]>=1:
#             temp.append(chr(i+ord('a'))+str(arr[i]))

    
#     return temp

# s = "aaabbc"
# print(occ(s))

s ="asdvvzzzz"
arr = [0]*26

for i in s:
    c = ord(i)
    index = c - ord('a')
    arr[index]+=1

for j in range(26):
    if arr[j]>=1:
        print(chr(j+ord('a'))+str(arr[j]),end=" ")
        
    
    
    