#wpp to find the MIN value of two numbers
def min_1(a,b):
    return min(a,b)
def min_2(a,b):
    return a if a<b else b

a=int(input('Enter te first number: '))
b=int(input('Enter te second number: '))
print('this is form min_1 function',min_1(a,b))
print('this is form min_2 function',min_2(a,b))
