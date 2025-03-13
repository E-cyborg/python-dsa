# row wise sum

a=[[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
sum=[]

for x in a:
    tmp = 0
    for y in x:
        tmp += y
    sum.append(tmp)

print(sum)