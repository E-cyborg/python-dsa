# doule the iteration O(logn)
def fun(num):
    i = 1
    c = 0
    while i < num:
        c += 1
        i *= 2
    return c

num = int(input('Enter the number: '))
print(fun(num))
