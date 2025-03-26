# number of digits in string

def fun(st):
    return len([x for x in st if x.isdigit])

n=input("enter the string: ")
print(fun(n))
