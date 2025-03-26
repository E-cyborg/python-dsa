# all divisor of n number
def fun1(num):
    result =[]
    if num ==0:
        return
    for i in range(1,num+1):
        if num %i == 0:
            result.append(i)
    return result
def fun2(num):
    return [i for i in range(1,num+1) if num%i==0]


print('---All divisor finder---\n\n')

num= int(input('Enter the number: ')
)
print('Funtion-1 : ',fun1(num))
print('Funtion-2 : ',fun2(num))