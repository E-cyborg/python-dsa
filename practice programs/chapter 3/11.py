#finding the factorial of given number
import math
def fun(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial
def fun2(num):
    return math.factorial(num)
def fun3(num):
    
    if num==0:
        return 1
    else:
        return num*fun3(num-1)
num=int(input('Entre the number to find factorial: '))
print('result: ',fun(num))
print('result: ',fun2(num))
print('result: ',fun3(num))