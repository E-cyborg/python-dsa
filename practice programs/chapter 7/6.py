# back tracking

def fun(n):
    if n== 0:
        return
    fun(n-1)
    print(n)

fun(6)
#Output:
# 1
# 2
# 3
# 4
# 5
# 6

