# number of consonants

def fun(st):
    a=[x for x in st if x not in ['a','e','i','o','u']]
    return f"{a} {len(a)}"

n=input("Enter the string: ")
print(fun(n))