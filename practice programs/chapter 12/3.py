
def liner(l,key):
    for x in range(len(l)-1,0,-1):
        if key == l[x]:
            return x
    return -1

list= [1,2,3,4,5,6,7,8,9,0,1]
print(list)
a=liner(list,1)
print(f"result: {a}")