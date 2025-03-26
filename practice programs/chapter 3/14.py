#reverse a number
def reverse(num):
    return int(str(num)[::-1])

def re2(num):
    r=0
    while num!=0:
        d=num%10
        r=r*10+d
        n=n//10
    return r

print('-----Welcome to reverse the number program-----\n')
num=input('Enter the number: ')

print(f'\nBefore: {num} and after reverse1 function: {reverse(num)}')
print(f'\nBefore: {num} and after reverse2 function: {reverse(num)}')