# print number 1 to n
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(10)