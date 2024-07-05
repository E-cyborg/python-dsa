#dependance inner loop to the outer loop O(n^2)
def fun(num):
    i=0
    c=0
    while i<num:
        j=0
        while j<i:
            c+=1 
            j+=1
        i+=1
    return c
num=int(input('Enter the number: '))
print(fun(num)) 