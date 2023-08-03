def num():
    x=int(input("enter number greater then 0 : "))
    try: 
        if x<=0:
            raise ValueError("error: enter number greater then 0")
    except ValueError as e:
        return e

print(num()) 



def num():
    x=int(input("enter number greater then 0 : "))
    try: 
        if x<=0:
            raise ValueError("error: enter number greater then 0")
    except ValueError as e:
        return e
    else:
        print("you have enterd right value")
    finally:
        print("may you understand")

print(num())
        