# prime number check
def fun(n,i):
    if i==1:
        return True
    elif n%i == 0:
        return False
    return fun(n,i-1)
    
print(fun(23,23//2))