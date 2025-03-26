# convert each word first char  and last char to upper case

def fun(st):
    return ' '.join([x[0].upper()+x[1:len(x)-1].lower()+x[-1].upper() if len(x)!=1 else x.upper() for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))