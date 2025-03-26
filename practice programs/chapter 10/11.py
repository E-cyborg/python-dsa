# convert the sting in lower case

# count special char

def fun(st):
    a=""
    for x in st:
        if ord(x)<=90:
            a=a+chr(ord(x)+32)
        else:
            a+=x
    return a

n=input("enter the string: ")
print(fun(n))