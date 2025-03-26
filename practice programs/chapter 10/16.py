#  reverse the words in string
def fun(st):
    return ' '.join([x[::-1] for x in st.split(" ")])

n = input("Enter the string: ")
print(fun(n))