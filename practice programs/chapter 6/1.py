# matrix programs
# read and write matrix elements


# my code 
r= int(input("Enter number of Rows: "))
c= int(input("Enter number of Column: "))

a=[]

for x in range(r):
    tmp = []
    for y in range(c):
        t=int(input(f"Enter the number for row: {x} col: {y}: "))
        tmp.append(t)
    a.append(tmp)

for x in a:
    for y in x:
        print(y,end=" ")
    print()


# sir code 

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of col: "))
lst= []
for x in range(r):
    tmp = [int(i) for i in input().split()]
    lst.append(tmp)

for x in lst:
    for y in x:
        print(y,end=" ")
    print()