#swap first and last element in the list

def fun1(lst):
    tmp =lst[0]
    lst[0] = lst[-1]
    lst[-1]=tmp
    return lst

def fun2(lst):
    lst[0],lst[-1] = lst[-1],lst[0]
    return lst

lst = [1,2,3,4,5,6,7]
print('===---| swaping the data first and last element in list |---===')
print(lst,'\n\n')
print('output fun1: ',fun1(lst[:]))
print('output fun2: ',fun2(lst[:]))