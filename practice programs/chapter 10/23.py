# remove the special char

def fun(st):
    l=[]
    for x in st:
        if x.isalnum():
            l.append(x)
    return ''.join(l)

n=input("Enter the string: ")
print(f"result: {fun(n)}")
