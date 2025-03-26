#Finding the maximum out of four numbers
def fun1(a,b,c,d):
    return a if a>b and a>c and a>d else b if b>c and b>a and b>d else c if c>a and c>b and c>d else d

def fun2(a,b,c,d):
    return max(a,b,c,d)

def fun3(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>c and b>a and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    else:
        return d
    

print('Finding the maximum out of four numbers')
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))
d=int(input('Entre the fourth number: '))

print('\n -----result----- \n')

# print('This inside the if else: ',a if a>b and a>c else b if b>c and b>a else c)
print('this inside the function1: ',fun1(a,b,c,d))
print('this inside the function2: ',fun2(a,b,c,d))
print('this inside the function3: ',fun3(a,b,c,d))
