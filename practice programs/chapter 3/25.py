#checking the if number is prime or not then checking the number factorial 

def fun1(num):
    result=0
    for i in range(2, num):
        if num % i == 0:
            
            return 'this is not a prime number'
    result=1     
    for i in range(1,num+1):
        result*=i
    return result

print('---Prime number factorial---\n\n')
num= int(input('Enter the number: '))
print('Version-1 checking...: ',fun1(num))