#Finding the maximum out of three numbers
def fun1(a,b,c):
    return a if a>b and a>c else b if b>c and b>a else c
def fun2(a,b,c):
    return max(a,b,c)
def fun3(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
    

print('Finding the maximum out of three numbers')
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))

print('\n -----result----- \n')

print('This inside the if else: ',a if a>b and a>c else b if b>c and b>a else c)
print('this inside the function1: ',fun1(a,b,c))
print('this inside the function2: ',fun2(a,b,c))
print('this inside the function3: ',fun3(a,b,c))
