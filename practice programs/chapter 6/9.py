# opposite diagonal sum

a= [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9,10,11,12]
    ]

# my code
sum =0
b=0

for x in range(len(a[0])-1,-1,-1):
    if b == len(a):
        break
    sum+=a[b][x]
    b+=1

print(sum)


# chatgpt

# Sum the elements on the diagonal starting from the top-right corner
sum = sum(row[-i - 1] for i, row in enumerate(a))
print(sum)