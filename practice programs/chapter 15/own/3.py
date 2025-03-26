# using function

def fun3():
    print("fun3")

def fun2():
    print("fun2 line: 1")
    fun3()
    print("fun2 line: 2")
def main():
    print("main line: 1")
    fun2()
    print("main line: 2")

main()


# output:-
# main line: 1
# fun2 line: 1
# fun3
# fun2 line: 2
# main line: 2