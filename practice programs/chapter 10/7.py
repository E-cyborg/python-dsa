# count number of spaces

def fun(n):
    return len([x for x in n if x ==" "])

n=input("enter the string: ")
print(fun(n))
