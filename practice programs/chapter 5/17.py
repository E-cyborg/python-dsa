# rotate the list by n enter number

def fun1(lst,n):
    for _ in range(n):
        a=lst[0]
        lst= lst[1:]
        lst.append(a)
    
    return lst
def fun2(lst,n):
    return lst[len(lst)//n:]+lst[:len(lst)//n]

def fun3(lst,n):
    if len(lst)<n:
        return "Rotation out of index"
    return lst[n:]+lst[:n]

def fun4(lst,n):
    for _ in range(n):
        lst.append(lst.pop(0))
    return lst


print(f"Result= {fun1([1,2,3,4,5],2)}")
print(f"Result= {fun2([1,2,3,4,5],2)}")
print(f"Result= {fun3([1,2,3,4,5],2)}")
print(f"Result= {fun4([1,2,3,4,5],2)}")