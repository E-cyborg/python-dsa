# return the logest plandrom
# base on split

def fun(st):
    l=""
    for x in st.split():
        if x==x[::-1] and len(x)>len(l):
            l=x

    return l if l else "no pelandrom in the string"

n=input("Enter the string: ")
print(f"Res: {fun(n)}")