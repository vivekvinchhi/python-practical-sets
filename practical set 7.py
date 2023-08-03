# -------------p1---------------------------------------------------
# j=open("C:/Users/vinch/Downloads/vivek.txt")
# print("using read : ",j.read())
# v=open("C:/Users/vinch/Downloads/vivek.txt")
# print("using readline : ",v.readline())
# i=open("C:/Users/vinch/Downloads/vivek.txt")
# print("using readlines : ",i.readlines())

# -----------------------------p2----------------------------------


with open('C:/Users/vinch/Downloads/vivek.txt', 'r') as f_in:
        with open('output.txt', 'w') as f_out:
        
            for line in f_in:
            
                a, b = map(int, line.strip().split())
            
                sum_ab = a + b
                prod_ab = a * b
                f_out.write(f"{a} {b} {sum_ab} {prod_ab}\n")
