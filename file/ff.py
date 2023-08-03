# f=open("abc.txt","r")
# f.seek(5)
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.close()

# f=open("ff.txt","a")
# f.write("hello vivek")
# t = (1, (9, 10), 7, 2)
# a, b, c, d = t
# print (b[1])

# l = [10, [45], [65, 65, 88, 99]]
# x = []
# for i in l:
#     if type(i) == list:
#         x = x + flatten(i)
#     else:
#         x.append(i)
# print(x)

# try:
#     f=open("ffg.txt","w")
#     try:
#         f.write("frffrfsfs")
#     except:
#         print("svfv")
#     finally:
#         print("dsrdsdxcsdsfdfvdxcv")
#         f.close()
# except:
#     print("ok")




# def nl(l):
#     for i in l:
#         if type(i)==list:
#             nl(i)
#         else:
#             z.append(i)
    
# l=[1,[5,6,7],8,[8,[9,12]]]
# z=[]
# # nl(l)
# # print(z)    

# def fibb(n):
#     x = [0, 1]
#     for i in range(2, n+1):
#         x.append(x[i-1] + x[i-2])
#     return x
    
# print(fibb(9))

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def detail(self):
        print(self.name)

class child(student):
    def vv(self):
        print(self.age)
x=child("vivek",20)
x.detail()
x.vv()
        
    