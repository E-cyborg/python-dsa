def fun1(num):
    temp = str(num)
    result=0
    for x in temp:
        result+=int(x)
    return result


def fun2(num):
    result=0
    temp=[int(x) for x in str(num)]
    for i in temp:
        result+=i
    return result


def fun3(num):
    s=0
    while num!=0:
        d=num%10
        s+=d
        num//=10
    return s

def fun4(num):
    return sum([int(x) for x in str(num)])

print('--- Finding the sum of digth in number ---\n\n')
num=int(input("Enter a number: "))


print('Function1 result= ',fun1(num))
print('Function2 result= ',fun2(num))
print('Function3 result= ',fun3(num))
print('Function4 result= ',fun4(num))