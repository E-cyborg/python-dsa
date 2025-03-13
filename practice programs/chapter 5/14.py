# Remove the dublicat elements from the list

def fun(l):
    for i,x in enumerate(l):
        l2=l[i+1:]
        for i,z in enumerate(l2):
            if z == x:
                del l[i+1]
    return l
def fun2(l):
    return list(set(l))

def fun3(l):
    c=[]
    for x in l:
        if x not in c:
            c.append(x)
    return c

print(f"result {fun([1,2,2,3,4])}")
print(f"result {fun2([1,1,1,1,2,2,3,4])}")
print(f"result {fun3([1,1,1,1,2,2,3,4])}")