# sum of each element in the matrix


# my code
matrix= [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
t_sum =0
for x in matrix:
    for y in x:
        t_sum+=y

print(t_sum)



# sir code
t_sum= 0
for x in matrix:
    t_sum+=sum(x)
print(t_sum)


# chapgpt
t_sum = sum([x for y in matrix for x in y])

print(t_sum)