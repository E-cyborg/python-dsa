# reverse the string
# my code 

def fun(s):
    if len(s) == 0 or len(s) ==1:
        return s

    return s[-1]+fun(s[:-1])
print(fun("kinshuk"))


# code from sir

def fun1(s):
    if len(s) ==0 or len(s) == 1:
        return s
    return fun1(s[1:])+s[0]
print(fun1("kinshuk"))