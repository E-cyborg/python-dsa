#half iterations
#the O(logn) logarithmic time complexity
def fun(num):
    i=num
    c=0
    while i>0:
        c=c+1
        i=i//2
    return c
    
num=int(input('Enter the number: '))
print(f' {num} the number of instruction in O(logn)) is:' ,fun(num))

#HOW THIS WORKING
#if num=100
#then i=num
# while i>0
# it will divide the i by 2     
# and the c will increment