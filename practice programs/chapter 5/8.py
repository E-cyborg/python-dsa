#count number of elements greeater then x

def fun1(lst,n):
    count= 0
    for x in lst:
        if x > n:
            count+=1
    return count

def fun2(lst,n):
    return len([i for i in lst if i>n])


lst= [1,23,4,4,5,46,3,52,54,23,4,34,234,532,534,5]
print('---===| Finding the greter element then n |---===')
print(lst)
n= int(input('Enter the num: '))


print('output fun1: ',fun1(lst,n))
print('output fun1: ',fun2(lst,n))