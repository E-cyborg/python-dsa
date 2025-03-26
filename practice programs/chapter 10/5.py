# count number of characters

def fun(st):
    return len([x for x in st if x.isalpha()])

n=input("enter the string: ")
print(fun(n))