#strong numbers

def funct(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial

def function1(num):
    result=0
    for i in num:
        result+=funct(int(i))
    if int(num) == result:
        return True
    return False

def for_range(num):
    result =[]
    for i in range(int(num)):
        temp =0
        for j in str(i):
            temp+=funct(int(j))
        if i == temp:
            result.append(i)
    return result


print('===--| Strong numbers|--===\n\n')
num = input('Enter the number: ')
print('Output-1: ',function1(num))
print('Output-2: ',for_range(num))