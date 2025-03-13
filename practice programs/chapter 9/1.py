# Du=ynamic programing 
# application 1--> fibonacci serise

def fun(a,b):
    global c
    c+=1
    if a>=40:
        return 
    print(a)
    fun(a+b,a)

c=0
print(fun(0,1))
print(c)


