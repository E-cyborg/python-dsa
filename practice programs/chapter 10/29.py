# password validation
# must be grater then or equal to 10 char  y
# atleast have one speacial char  y
# atleast have one upper case char y
# atleast have one lower case char  y
# atleast have one numaaric char y

def fun(st):
    if not len(st)>=10:
        return False
    if not any(char.isupper() for char in st):
        return False
    if not any(char.islower() for char in st):
        return False
    if  all(char.isalnum() for char in st):
        return False
    if not any(char.isdigit() for char in st):
        return False
    return True

n=input("Entet the string: ")
print(f"Res: {fun(n)}")
