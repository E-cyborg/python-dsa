# addition of two matrix 2D


a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
sum=[]
for x in range(len(a)):
    tmp = [a[x][y]+b[x][y] for y in range(len(a))]
    sum.append(tmp)

print(sum)