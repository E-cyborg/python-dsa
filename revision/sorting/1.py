def buble_sort(l:list):
    a=len(l)-1
    while a:
        for x in range(0,a):
            if l[x]>l[x+1]:
                l[x+1],l[x]=l[x],l[x+1]
        a-=1

    print(l)

list=[1,3,4,6,7,3,2]
print(buble_sort(list))


# done in first try