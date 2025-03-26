#find second lagrest number in list

def fun1(lst):
    gr=0
    se=0
    for  x in lst:
        if x>gr:
            se =gr
            gr=x
    return se

lst = [1,2,3,4,5]

print('---| Finding the second largest num |---')
print(lst,'\n\n')
print('Output: ',fun1(lst))