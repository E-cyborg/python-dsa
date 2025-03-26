# even index to upper odd to lower

def fun(st):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(st))

n = input("Enter the string: ")
print(fun(n))
