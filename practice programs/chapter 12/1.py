# seacrching 
# there are two types of algo of searching 

# 1- liner searching --go all over the list
# 2- binary searching -- divide the list in half and another half until it reach | the list have to be sorted


# liner

def liner(l,key):
    for x in range(len(l)):
        if key == l[x]:
            return x
    return -1

list= [1,4,23,2,36,2,34,634,6,34,3,3,34,34,34,34,346,7,7,3,65,7,8,6,4]
print(list)
a=liner(list,1)
print(f"result: {a+1}")