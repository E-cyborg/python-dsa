# iterative power
from math import pow

def fun1(a,b):
    return a**b


def fun2(a,b):
    return pow(a,b)

def fun3(a,b):
    temp=1
    for i in range(0,b):
        temp= temp*a
    return temp

print('--- This is a power function---\n\n')

print("Enter two numbers: ")
a=int(input())
b=int(input())

print('From the version-1: ',fun1(a,b))
print('From the version-2: ',fun2(a,b))
print('From the version-3: ',fun3(a,b))