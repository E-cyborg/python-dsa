# identity matrix or not


# test code
a=[[1, 0,0], 
    [0, 1, 0],
    [0,0,1]
    ]
b=[]

for x in range(len(a)):
    b.append(a[x][x])
t= b[0]

if all(x==t for x in b):
    print("it is a identity matrix")
else:
    print("it is not a identity matrix")

if all(a[x][x] == 1 for x in range(len(a))) and all(a[x][y] ==0 for x in range(len(a)) for y in range(len(a[0])) if x!=y):
    print(True)
else:
    print(False)