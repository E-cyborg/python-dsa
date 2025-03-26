# selection sorting
def sel_sort(l:list):
    le=len(l)
    for x in range(le-1):
        mi=x
        for j in range(x+1,le):
            if l[mi]>l[j]:
                mi=j
        l[mi],l[x]=l[x],l[mi]
    return l

list=[1,2,54,6,7,3,2]
print(sel_sort(list))