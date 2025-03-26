# sorting chapter 11 
# there are two build in method for sorting

# list.sort()

a=[1,5,9,8,7,2,3,6,4]
print(a)
a.sort()
print(a)


# list.sort () using key argumnet it use to sort the list useing a fun build by user

# eg:
def fun(s):
    return len(s)

ls= ["kin","kinshuk","kik","kiku","lil"]

ls.sort(key=fun)
print(ls)

# this is sorting the list based on the length of a element



# sorted function
a=[1,5,9,8,7,2,3,6,4]
print(a)
a=sorted(a)
print(a)

