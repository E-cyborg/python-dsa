# bubble sort()

l=[1,5,2,3,4]
n=len(l)
for x in range(n):
    for y in range(n-x-1):
        if l[y]>l[y+1]:
            l[y],l[y+1]=l[y+1],l[y]
print(l)


# this is in acending order

# for dec
#  change the comparion operter to <
