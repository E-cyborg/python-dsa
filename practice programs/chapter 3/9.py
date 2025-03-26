#finding the absolute value 
def abs1(num):
    if num<0:
        return -num
    else:
        return num

num=int(input('Enter number: '))
print('the absolute value from function1:',abs1(num))
print('the absolute value from abs:',abs(num))