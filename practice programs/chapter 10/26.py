#check if the string is rotated or not

def fun(st1,st2):
    if len(st1) != len(st2):
        return False
    for x in range(len(st1)):
        st2=st2[1:]+st2[0]
        if st2== st1:
            return True
    return False

n=input("Enter the 1 string: ")
m=input("Enter the 2 string: ")

print(f"Res: {fun(n,m)}")


# best case
def fun(n,m):
    tmp=n+n
    return tmp.find(m) !=-1

print(f"Res: {fun("abc","bca")}")