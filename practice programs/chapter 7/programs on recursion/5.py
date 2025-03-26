# check if string is palandrom or not
def fun(str,st,en):
    if st>=en:
        return True
    return str[st] == str[en] and fun(str,st+1,en-1)
print(fun("kik",0,2))

# insane 