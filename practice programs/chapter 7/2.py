def fun1(n):
    if n<=0:
        return
    print("hello there")
    fun1(n-1)

fun1(-3)