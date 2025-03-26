#wpp to find the max value of two numbers
def max_fun(a,b):
    return max(a,b,)

def if_stat(a,b):
    return a if a>b else b



a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
print('\n -------result------- \n')
print('max fuction: ',max_fun(a,b))
print('if statement: ',if_stat(a,b))
