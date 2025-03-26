#find oddd and even number

def fun(num):
    return 'Even' if num%2==0 else 'Odd'

num=int(input('Enter the number: '))
print('\n -------result------- \n')
print('THis is inside if else: ','Even' if num%2==0 else 'Odd')
print('this inside the function: ',fun(num))
print('THis is from the bitwise oprator: ','Even' if (num&1)==0 else 'Odd')