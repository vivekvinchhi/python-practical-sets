#  Selection sort

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if min >arr[j]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

s = [1,5,8,3,21,2,4]
print(selection(s))


d=[1,1,2,3,4,3,5,2]
index = 0
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if d[i]==d[j]:
            d.pop(d[j])
            break

print(d)
f=[]
for i in d:
    if i not in f:
        f.append(i)
print(f)

g=[]
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if d[i]==d[j] and d[i] not in g:
            g.append(d[i])
            
print("g is ",g)

result =0
for i in range(len(d)):
    result ^=d[i]

print(result)

z = [1,2,1,4,5,7,4,5]

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        l=set()
        for i in range(n-2):
            j = i+1
            k = n-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                
                        l.add((nums[i],nums[j],nums[k]))
                        j+=1
                        k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1          
        return l

aa=[-1,0,1,2,-1,-4]
obj1 = Solution()
re=obj1.threeSum(aa)
print(re)

    