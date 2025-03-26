def fun1(num):
    count=0
    while num > 0:
        count+=1
        print(num%10)
        num //= 10
    return count
num=int(input('Enter the num: '))
print('function1: ',fun1(num))