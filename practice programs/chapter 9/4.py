# climing stairs
# can only that 1 or 2 step at a time 

def fun(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return fun(n-1) +fun(n-2) 

for x in range(5):
    print(f"{x}:={fun(x)}")