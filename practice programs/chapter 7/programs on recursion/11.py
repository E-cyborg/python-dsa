# permutations of a given string

def fun(str,ans):
    if len(str) == 0:
        print(ans)
        return
    for x in range(len(str)):
        fun(str[:x]+str[x+1:],ans+str[x])

fun(str="kamal",ans="")