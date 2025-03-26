#left shift by 1 element
def fun1(lst):
    tmp = lst[0]
    res= []
    del lst[0]
    for x in lst:
        res.append(x)
    res.append(tmp)
    return res
def fun2(lst):
    x=0
    while x <= len(lst):
        lst[x]>>1
        x+=1
    return lst
    
def fun3(lst):
    tmp = lst[0]
    del lst[0]
    lst.append(tmp)
    return lst
lst= [1,2,3,4,5]
print('output: ',fun2(lst))