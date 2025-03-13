# leaner algebra multiplication of two matrix

a=[[1,2],
   [4,5]]
b=[[6,7],
   [9,0]]
for i,x in enumerate(a):
    for j,y in enumerate(a[0]):
        a[i][j]=a[i][j]*b[j][i]

for x in a:
    print(x)
