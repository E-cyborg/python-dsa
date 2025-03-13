# get the index of given element

def fun1(lst,n):
    ind=0
    for x in lst:
        if x == n:
            return ind
        ind+=1
    return -1

lst =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print('===---| Index of the given element |---===')
print(lst,'\n\n')
n=int(input('Enter the number: '))
print('output fun1: ',fun1(lst,n))