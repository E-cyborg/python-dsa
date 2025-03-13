#check if the string is anagrams 

def fun(n,m):
    for x in n:
        if x not in m:
            return False
        
    return True

n=input("Enter the 1 string: ")
m=input("Enter the 2 string: ")

print(f"Result: {fun(n,m)}")

