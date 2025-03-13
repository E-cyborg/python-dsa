# rotate the matrix by 90°
arr= [[1,2,3],
      [5,6,7,],
      [9,0,1,]]
new = []
for x in range(len(arr)):
    tmp=[]
    for y in range(len(arr[0])):
        tmp.append(arr[y][x])
    new.insert(0,tmp)

for x in new:
    print(x)