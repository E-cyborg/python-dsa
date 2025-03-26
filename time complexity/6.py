def fun(n):
    c=0
    i=n
    while i >0:
        j=0
        while j < i:
            c+=1
            j+=1
        i=i//2
    return c
n=int(input('Enter the number: '))
print(fun(n))
# O(logn)