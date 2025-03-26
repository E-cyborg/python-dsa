#finding the sum of n natural numbers
def result(num):
    sum=0
    for i in range(0,num+1):
        sum+=i
    return sum
def result2(n):
    return n*(n+1)//2

def rec(num):
    
    if num==0:
        return 0
    else:
        return num+rec(num-1)
    
print('----------finding the sum of n natural number----------\n')
num=int(input('Enter the number: '))
print(f'result={result(num)}\n')
print(f'result={result2(num)}\n')
print(f'result={rec(num)}\n')