#union for a list

def fun1(l1,l2):
    q=[]
    for x in l1:
        if x not in q:
            q.append(x)
    for x in l2:
        if x not in q:
            q.append(x)
    return q

def fun2(l1,l2):
    l= l1+l2
    lst= []
    for x in l:
        if x not in lst:
            lst.append(x)
    return(lst)

def fun3(l1,l2):
    return list(set(l1+l2))

l1=[1,2,3,4,5]
l2 = [4,5,6,7,8,9]

print(f"Result: {fun1(l1,l2)}")
print(f"Result: {fun2(l1,l2)}")
print(f"Result: {fun3(l1,l2)}")