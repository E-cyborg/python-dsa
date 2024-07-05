#sum of all the elements present in the list 
from functools import reduce

def for_loop(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum

def sum_fun(lst):
    return sum(lst)


def reduce_fun(lst):
    return reduce(lambda x , y: x+y ,lst)

# def map_fun(lst):
#     return map(lambda x:x+10,lst)

lst=[1,2,3,4,5,6,7,8,9,10]
print('This is inside from for_loop function: ',for_loop(lst))
print('This is inside from sum_fun function: ',sum_fun(lst))
print('This is inside from reduce function: ',reduce_fun(lst))

# print(map_fun(lst))