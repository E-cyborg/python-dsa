# count the number of accurence 

a="abcdcda"
b="cd"
c=0
for x in range(len(a)):
    if a[x] == b[0]:
        if all(a[x+y]==b[y] for y in range(len(b))):
            c+=1

print(c)