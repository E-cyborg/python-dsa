# all the occurrence in the list


def liner(l,key):
    out=[]
    for x in range(len(l)):
        if key == l[x]:
            out.append(x)
    return out

list= [1,2,3,4,5,6,7,8,9,0,1]
print(list)
a=liner(list,1)
print(f"result: {a}")