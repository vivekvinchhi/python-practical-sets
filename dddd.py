def create_dict(list1,list2):
    d=dict()
    for i in list1:
        for j in list2:
            d[i]=j
            list2.remove(j)
            break
    return(d)

l1=[1,2,3,45,6,8]
l2=[45,55,66,88,99,22]
print(create_dict(l1,l2))