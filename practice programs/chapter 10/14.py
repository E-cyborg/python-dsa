# even reverse odd no reverse
def fun(st):
    return ' '.join([x[::-1] if len(x)%2==0 else x for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))