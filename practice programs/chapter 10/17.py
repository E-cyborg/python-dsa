# convert each word first char to upper case

def fun(st):
    return ' '.join([x[0:1].upper()+x[1:].lower()  for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))