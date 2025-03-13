# recursion

# the process in whicha function call it self is know as recuresion

# types 

# direct --> a function call it self

# indirect --> a function fun2() call fun1() and fun1() call fun2() and fun2() call fun1()

# finate --> terminate at a point
# in finate --> never terminates (RecuresionError -- Runtime Error)



#syntax 

# def fun(n):
    # basse condition
#     ------------------
#     ------------------
#     ------------------
    #      fun(n)
    # there should be a change in any parameter to satisfy the base condition


# application
# tree
# linked list
# graph
# sudoku 
# searching 
# sorting
# mathamaticall oprations(prime number,lcm,factorial)


# memory management in recuresion 
# 1 it use more momory
# 2 it use stack data structure
# 3 lifo last in first out
# 4 stack contain complete info about fun calls with parameter


# tails recursion 
# a recursive function is called tail recursive if the funtiondoes not do any thing after the last recursive  call 
# 5.py

# back teracking
# it is opposite of tails recursion after the last recursion call it will do somting and goes back to it will do again something it will reepeate till n
# 6.py


def fun():
    print("hello there")
    fun()
fun()