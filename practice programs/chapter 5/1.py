#sum of elements in a list
def fun1(lst):
    return sum(lst)

def fun2(lst):
    result=0
    for x in lst:
        result+=x
    return result

def fun3(lst):
    x = 0
    re = 0
    while x < len(lst):
        re += lst[x]
        x += 1
    return re

def fun4(lst):
    s=0
    for x in lst:
        s+=x
    return s
lst= [1,2,3,4,5,6,7,8]
print('---| Sum of list |---')
print(lst,'\n\n')
print('Output of fun1: ',fun1(lst))
print('Output of fun2: ',fun2(lst))
print('Output of fun3: ',fun3(lst))
print('Output of fun4: ',fun4(lst))
