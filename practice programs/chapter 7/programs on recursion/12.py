# find all the subset of gieven string

def fun(s,a,i):
    if i==len(s):
        print(a)
        return
    fun(s,a+s[i],i+1)
    fun(s,a,i+1)
fun("kinshuk","",0)