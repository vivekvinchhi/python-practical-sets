# class KSV:
#     cnt=0
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         KSV.cnt=KSV.cnt+1
#     def get_value(self):
#         return self.x,self.y
#     def print_value(self):
#         print(f"x: {self.x}, y: {self.y}")

# k1 = KSV(10, 20)
# print(k1.get_value())
# k1.print_value()
# print(KSV.cnt)
# print(k1.cnt)
        
# class Addition:
#  def __init__(self, x, y):
#     self.x = x
#     self.y = y
#  def __add__(self, other):
#     x = self.x + other.x
#     y = self.y + other.y
#     return Addition(x, y)
#  def __str__(self):
#     return f"({self.x}, {self.y})"
# v1 = Addition(1, 2)
# v2 = Addition(3, 4)
# result = v1 + v2
# print(result)

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and year%400==0:
        return True
    else:
        return False
    
    return leap

year = int(input())
        