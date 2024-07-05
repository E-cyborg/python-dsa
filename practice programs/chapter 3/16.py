# trailing zeroes of Factorial
from math import factorial

def check1(a):
    c=0
    if a[-1] != '0':
        return 0
    else:
        while a[-1] == '0':
            c+=1
            a=a[:-1]
        return c
a=input('Enter the number: ')
print('the factorial is ',factorial(int(a)))
a=str(factorial(int(a)))
print(f'the num of zero are: {check1(a)}')