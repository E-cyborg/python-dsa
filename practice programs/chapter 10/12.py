# swap case
def fun(st):
    a=""
    for x in st:
        if ord(x)<90:
            a+=chr(ord(x)+32)
        else:
            a+=chr(ord(x)-32)
    return a
n=input("enter the string: ")
print(fun(n))