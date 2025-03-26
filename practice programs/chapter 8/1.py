# Chapter-8 Backtracking

# • It is a method by which a solution found by moving/searching through large volume of data with some boundary conditions.

# • Eg

# •Number locks

# •Rat in maze

# •N-Queens

# Grid Based problems

# Sudoku

# #types of backtracking.

# decision based problems--> yes/n0
# Optimized solution based problems only one bestsolu
# Enumeration basec problems all possible salu

# Backtracting with list

# N-Queens

# Grid ways

# suduko problems



def fun(l,i,v):
    if len(l) == i:
        return 

    l[i]=v
    fun(l,i+1,v+1)
    l[i] = l[i]-1       # backtracking it will run after the function returning the proccess

l=[1,1,1,1,1]
fun(l,0,1)
print(l)

# after the recursion we preform a task that will effect the output that procees is know as backtracking