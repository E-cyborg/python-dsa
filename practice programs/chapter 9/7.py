#knapsack using dynamic programing
def fun(w,wts,va,n):
    dt=[[0 for x in range(w+1)]for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wts[i-1]<=j:
                dt[i][j]=max(dt[i-1][j],dt[i-1][j-wts[i-1]]+va[i-1])
            else:
                dt[i][j]=dt[i-1][j]
    return dt[n][w]

wts=[5,4,6,3]
va=[10,20,30,50]
w=10
n=4
print(fun(w,wts,va,n))