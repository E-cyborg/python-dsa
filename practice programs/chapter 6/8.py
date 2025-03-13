# diagonal sum 

a=[[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
ele = 0

for x in range(len(a)):
    for y in range(len(a[0])):
        if x==y:
            ele+= a[x][y]

print(ele)