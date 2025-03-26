# sum of digits of give number

def fun(n):
    if n<10:
        return n
    return n%10+fun(n//10)


print(fun(12218))