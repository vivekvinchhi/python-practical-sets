def permutation(arr,l,index):
    if index>=len(arr):
        l.append(arr[:])
        return 
    
    for j in range(index,len(arr)):
        arr[index],arr[j]= arr[j],arr[index]
        # print("before recursive call")
        # print("index  : ",index," j : ",j)
        # print(arr)
        # print()
        permutation(arr,l,index+1)
        # print("after recursive call")
        # print("index  : ",index," j : ",j)
        # print(arr)
        # print()
        arr[index],arr[j]= arr[j],arr[index]
        

l=[]
index = 0
arr = [1,2,3]
permutation(arr,l,index)
print(l)