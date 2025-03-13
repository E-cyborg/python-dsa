# factorial using recursion

def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)

print(fun(4))

# this is insane how it works

# let seen
#  return fun(n-1) n=3 will provide 
