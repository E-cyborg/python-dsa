#sum of odd numbers 


def fun1(num):
    return sum([int(x) for x in str(num) if (int(x)%2!=0)])


def fun2(num):
    s=0
    while num!=0:
        d=num%10
        if d%2 !=0:
            s+=d
        num//=10
    return s


print('--- sum of odd digits in anumber ---\n\n')


num= int(input('Enter the number: '))
print('version-1: ',fun1(num))
print('version-2: ',fun2(num))