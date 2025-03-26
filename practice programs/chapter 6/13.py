# swap two col

ls=[[1, 2, 3 ], 
    [4,5, 6, ],
    [7,8,9]]

a,b = [int(input("enter the two values: ")) for x in range(2)]

if a<len(ls)>=b:
    for x in ls:
        x[a],x[b] = x[b],x[a]

print(ls)