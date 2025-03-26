#check if the list is sorted or not

def fun1(lst):
    return True if lst == sorted(lst) else False

def fun2(lst):
    lt=float('-inf')
    print(lt)
    for x in lst:
        if x< lt:
            return False
        lt =x
    return True


lst=[-1,2,3,4,5,6,7]
print('===---| Checking if the list is sorted or not |---===')
print(lst,'\n\n')
print('output fun1: ',fun1(lst))
print('output fun2: ',fun2(lst))