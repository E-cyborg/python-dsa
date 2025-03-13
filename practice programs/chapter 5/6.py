#generate 10 random number between 0,20 and append them to a list

import random

def fun1():
    return [random.randint(0,20) for _ in range(0,10)]

def fun2():
    lst=[]
    for x in range(0,10):
        lst.append(random.randint(0,20))
    return lst

def fun3():
    x=1
    lst= []
    while x<= 10:
        lst.append(random.randint(0,20))
        x+=1
    return lst

print('---===| generate 10 random number between 0,20 and append them to a list |===---')

print(f'output fun1: {fun1()}')
print(f'output fun2: {fun2()}')
print(f'output fun3: {fun3()}')
