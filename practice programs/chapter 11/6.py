# counting sort 

def fun(l,n):
    out=[0]*len(l)
    count= [0]*n

    for x in l:
        count[x]=count[x]+1

    for x in range(1,len(count)):
        count[x] +=count[x-1]
    for x in reversed(l):
        out[count[x]-1]=x
        count[x]=count[x]-1
    for x in range(len(l)):
        l[x]=out[x]
    return
l=[1,3,1,3,5,4]
n=6
fun(l,n)
print(l)

# my count sort

l=[1,4,12,2,5,21,4,2]
n=22

co=[0]*22

for x in l:
    co[x]+=1
n=[]
for i,x in enumerate(co):
    for y in range(x):
        n.append(i)
print(n)