# count sorting

def count_sorting(l:list):
    tl=[0]*(max(l) + 1)
    new=[]
    for x in l:
        tl[x]+=1
    for i,x in enumerate(tl):
        for y in range(x):
            new.append(i)
    return new   

list=[1,2,5,6,7,3,2,60]
print(count_sorting(list))