def fun(t,w,v,n):
    if n==0 or w==0:
        return 0
    if w[n-1]>t:
        return fun(t,w,v,n-1)
    return max(v[n-1]+fun(t-w[n-1],w,v,n-1),fun(t,w,v,n-1))

w=[5,4,6,3]
v=[10,20,30,50]
t=10
print(fun(t,w,v,4))
