# count number of vowels

vo=['a','e','i','o','u']

n=input("Enter the string: ")
i=0
c=0
while i<len(n):
    if n[i] in vo:
        c+=1
    i+=1

print(f"vowels:= {c}")


def fun(st):
    return [x for x in st if x in ('a','e','i','o','u')]

print(fun('kinshuk'))