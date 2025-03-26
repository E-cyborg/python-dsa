# swaping diagonal elements
arr= [[1,2,3],
      [5,6,7,],
      [9,0,1,]]
j = -1
for i,x in enumerate(arr):
    x[i],x[j] = x[j],x[i]
    j-=1

for x in arr:
    print(x)