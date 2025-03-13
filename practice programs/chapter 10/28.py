#pangram all the alpabent with in a string
def fun(m):
    for x in range(97,123):
        if chr(x) not in m:
            return False
        
    return True

n=input("Enter the string: ")

print(f"Result: {fun(n)}")

