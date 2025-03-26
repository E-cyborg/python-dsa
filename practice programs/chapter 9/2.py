l=[None]*100

def fun(n):
    global c
    c+=1
    if l[n] !=None:
        return l[n]
    if n==0 or n==1:
        l[n]=n
    else: 
        l[n] = fun(n-1)+fun(n-2)
    return l[n]

c=0
fun(6)
print(l)
print(c)