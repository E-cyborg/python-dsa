#paliandrime number
def fun1(a):
    return a==a[::-1]
def re2(a):
    a=int(a)
    orignal=a
    r=0
    while a!=0:
        d=a%10
        r=r*10+d
        a=a//10
    return r == orignal

a=input('Enter the number to check: ')
print(f'check...{fun1(a)}')
print(f'check...{re2(a)}')