# previous proccess using memoization


# my code 
n=int(input("Enter the nnumber of stairs: "))
a=0
b=1
if n in (0,1):
    print(1)
    quit()
for x in range(n+1):
    a,b=a+b,a
    print(f"for {x} no of stairs: {a}")

# code from the coures
def fun(n):
    if n == 0:
        return 1  # Base case

    li = [0 for _ in range(n+1)]
    li[0] = 1  # Base case
    if n > 0:
        li[1] = 1  # Fibonacci-like sequence starts

    for x in range(2, n+1):
        li[x] = li[x-1] + li[x-2]

    return li[n]

for x in range(10):
    print(f"{x} ===> {fun(x)}")
