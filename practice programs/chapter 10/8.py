# count special char

def fun(st):
    return len([x for x in st if not x.isdigit() and not x.isalpha()])

n=input("enter the string: ")
print(fun(n))