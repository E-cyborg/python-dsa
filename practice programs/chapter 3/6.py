#Finding the maximum out of five numbers
def fun1(a,b,c,d,e):
    return a if a>b and a>c and a>d and a>e else b if b>c and b>a and b>d and b>e else c if c>a and c>b and c>d and c>e else d if d>a and d>b and d>c and d>e else e

def fun2(a,b,c,d,e):
    return max(a,b,c,d,e)

def fun3(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        return a
    elif b>c and b>a and b>d and b>e:
        return b
    elif c>a and c>b and c>d and c>e:
        return c
    elif d>a and d>b and d>c and d>e:
        return d
    else:
        return e

print('Finding the maximum out of four numbers')
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))
d=int(input('Entre the fourth number: '))
e=int(input('Entre the fivth number: '))

print('\n -----result----- \n')

print('this inside the function1: ',fun1(a,b,c,d,e))
print('this inside the function2: ',fun2(a,b,c,d,e))
print('this inside the function3: ',fun3(a,b,c,d,e))
