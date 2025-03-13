# remove dublicates fro the string

def fun(st):
    n=[]
    for x in st:
        if x not in n:
            n.append(x)
    return "".join(n)

print(fun("kinshuk"))