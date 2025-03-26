# swap two rows
ls=[[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

a,b = [int(input("enter the two values: ")) for x in range(2)]
if a< len(ls)>=b:
    ls[b],ls[a] =ls[a],ls[b]
print(ls)