# seprate even odd numbers form list

def fun1(lst):
    odd =[]
    even =[]
    for i in lst:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

def fun2(lst):
    a=[x for x in lst if x%2 == 0]
    b=[x for x in lst if x%2 != 0]
    return a,b


print('===---| odd even number seperator |---===')
lst=[]
while True:
    a=input('Enter the numbers:')
    if a == '':
        break
    
    else:
        lst.append(int(a))
        a=None

print('List: ',lst,'\n\n')



a,b=fun1(lst)
print(f'output fun1 :- odd: {a} | even {b} ')
a,b=fun1(lst)
print(f'output fun2 :- odd: {a} | even {b} ')