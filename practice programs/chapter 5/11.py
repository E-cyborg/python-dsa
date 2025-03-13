# find the largest/greatest  number in the list
def fun1(lst):
    return max(lst)

def fun2(lst):
    gr=0
    for x in lst:
        if gr< x:
            gr= x
    return gr



lst = [1,2,3,4,5,56]
print('---| Finding the greatest number in the list |---')
print(lst ,'\n\n')
print('output fun1: ',fun1(lst))
print('output fun2: ',fun2(lst))