#return the element index which appears greater then len(list)//2 


def fun1(l1):
    a=len(l1)//2
    l=[]
    for i,x in enumerate(l1):
        if l1.count(x) >= a and i not in l:
            l.append(i)
    return l if l else -1

l1=[1,1,12,12,1,12,3,3,1,31,1,1,1,1,1]
print(f"Result : {fun1(l1)}")