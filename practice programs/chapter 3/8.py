#swaping the values of two variables
def fun1(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def fun2(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
def fun3(a,b):
    a,b=b,a
    return a,b
def fun4(a,b):
    a=a*b
    b=a//b
    a=a//b
    return a,b
def fun5(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
def fun6(a,b):
    a=a+b-(b:=a)
    return a,b


a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
print('\n -----result-----\n')
print('This is inside the function1: ',fun1(a,b))
print('This is inside the function2: ',fun2(a,b))
print('this is inside the function3: ',fun3(a,b))
print('This is inside the function4: ',fun4(a,b))
print('This is inside the function4: ',fun5(a,b))
print('This is inside the function4: ',fun6(a,b))


print('\n first function is using another variable \n and the second function is not using any third variable')