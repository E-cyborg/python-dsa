# subtractio in 2d list


b=[[1,2,3],[4,5,6],[7,8,9]]
a=[[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

sum=[]
for x in range(len(a)):
    tmp = [a[x][y]-b[x][y] for y in range(len(a))]
    sum.append(tmp)

print(sum)