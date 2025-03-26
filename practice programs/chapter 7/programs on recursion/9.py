# fib seq
def fun(n):
    if n==0 or n==1:
        return n
    return fun(n-1) + fun(n-2)
for x in range(10):
    print(fun(x))