def fun(st):
    return True if st == st[::-1] else False

st=input("ENter the string: ")
print(f"Result: {fun(st)}")