#gridways

def fun(i,j,m,n):
    if i==m-1 and j==n-1:
        return 1
    if i == m or j ==n:
        return 0
    v1= fun(i+1,j,m,n)
    v2= fun(i,j+1,m,n)
    return v1+v2


n,m = 3,4
print(fun(0,0,m,n))