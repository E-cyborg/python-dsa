# return middle char or characters

def fun(st):
    return ''.join([st[int(len(st)/2)] if len(st)%2==0 else st[(len(st)//2)-1]+st[len(st)//2]])
print(fun("kinshukk"))