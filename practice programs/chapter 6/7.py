# column wise sum
a=[[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]

sum =[0,0,0,0]

for x in range(len(a)):
    for y in range(len(a[0])):
        sum[y]+=a[x][y]


print(sum)