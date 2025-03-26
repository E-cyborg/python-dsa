# convert even to upper and odd to lower words not char 
def fun(st):
    return ' '.join([x.upper() if len(x)%2==0 else x.lower() for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))