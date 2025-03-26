# intersection of two list

def fun1(l1,l2):
    l=[]
    for x in l1:
        if x in l2:
            l.append(x)

    return l 

l1=[1,2,3,4,5,0]
l2=[4,5,6,7,8,9]
print(f"Result: {fun1(l2,l1)}") 