# tower of hanoi
def fun(n,s,t,d):
    if n==1:
        print(f"move dic 1 form {s} to {d}")
    else:
        fun(n-1,s,d,t)
        print(f"move dic {n} form {s} to {d}")
        fun(n-1,t,s,d)

fun(4,"s","t","d")