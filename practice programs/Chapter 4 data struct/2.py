from math import factorial
print("====----- Dictionary comprehension----====\n\n")
ran =int(input('Enter the range to perform : '))
factorial_dict = {i: factorial(i) for i in range(1, ran+1)}
print(factorial_dict,'\n')

squre_dict= {i:i**i for i in range(1,ran+1)}
print(squre_dict,'\n')

