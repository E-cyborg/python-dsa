#merge to list into one

def fun1(l1,l2):
    for x in l2:
        l1.append(x)
    return l1

def fun2(l1,l2):
    return l1+l2


def fun3(l1,l2):
    print(l1,l2)
    return sum(l1,l2)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

print(f"result: {fun1(l1,l2)}")
print(f"result: {fun2(l1,l2)}")
print(f"result: {fun3(l1,l2)}")