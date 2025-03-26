# transpose the matrix
import copy
a= [[1, 2, 3], 
    [5, 6, 7],
    [9,10,11]
    ]


#my code
b=copy.deepcopy(a)

for i,x in enumerate(b):
    for j,y in enumerate(x):
        a[i][j] = b[j][i]

print(a)


# sir code
for x in range(len(a)):
    for y in range(len(a[0])):
        print(a[y][x],end=" ")
    print()