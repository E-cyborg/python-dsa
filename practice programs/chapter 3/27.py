
def fun2(num):
    return [i for i in range(1,num+1) if num%i==0]


def fun1(number):
    l_of_number = []
    if number <= 0:
        return False
    
    for num in range(1, number + 1):
        sum_of_divisors = 0
        
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        
        if sum_of_divisors == num:
            l_of_number.append(num)
    
    return l_of_number

print('---- Finding the perfect numbers ----\n\n')
number = int(input('Enter the range: '))
print('Function-1:', fun1(number))
