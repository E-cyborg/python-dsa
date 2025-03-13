# selection sorting 
# selection an element and fix in its position
# first min element in first index
# second min element in second index


def fun(l):
    for x in range(len(l)):
        min_num=x
        for z in range(x+1,len(l)):
            if l[z]<l[min_num]:
                min_num=z
        l[x], l[min_num] = l[min_num], l[x]
    print(l)
l=[1,4,12,12,4,53,212]
fun(l)