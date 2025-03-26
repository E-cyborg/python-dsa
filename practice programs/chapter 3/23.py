#sum of prime numbers 


def fun1(num):
    return sum([int(x) for x in str(num) if x in '2357'])


def fun2(num):
    s=0
    while num!=0:
        d=num%10
        if d==2 or d==3 or d==5 or d==7:
            s+=d
        num//=10
    return s


print('--- sum of prime digits in anumber ---')
num= int(input('Enter the number: '))
print('version-1: ',fun1(num))
print('version-2: ',fun2(num))