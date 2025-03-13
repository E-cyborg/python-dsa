# convert each word first char  and last char to lower case and other to upper

def fun(st):
    return ' '.join([x[0].lower()+x[1:len(x)-1].upper()+x[-1].lower() if len(x)!=1 else x.lower() for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))