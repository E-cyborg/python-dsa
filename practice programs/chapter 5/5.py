#get the smaller element form a list lesser then the given element x

def fun1(lst,num):
    sm=0
    for i in lst:
        if i<num and i>sm:
            sm=i
        else:
            continue

    return sm 

def fun2(lst,num):
    return [x for x in lst if x<num]

print('---===| Get the smaller element form a list lesser then the given element x |===---')
lst=[]
while True:
    a=input('Enter the numbers:')
    if a == '':
        break
    
    else:
        lst.append(int(a))
        a=None
num = int(input('Enter the number to find smaller then that :'))
print('List: ',sorted(lst),'\n\n')


print(f'output of fun1: {fun1(lst,num)}')
print(f'output of fun2: {fun2(lst,num)}')
