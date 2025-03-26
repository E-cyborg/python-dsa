#--- COUNTING THE DIGITS

def fun1(num):
    count=0
    while num > 0:
        count+=1
        num //= 10
    return count
def fun2(num):
    return len(str(num))
def fun3(num):
    if num == 0:
        return 0
    else:
        return 1+fun3(num//10)
num=int(input('Enter the num: '))
print('function1: ',fun1(num))
print('function2: ',fun2(num))
print('function3: ',fun3(num))