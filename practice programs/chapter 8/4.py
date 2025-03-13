def p_su(su):
    for x in su:
        print(" ".join(map(str, x)))
    print()



def check(su,r,c,v):
    # row check
    for x in range(9):
        if su[r][x] == v:
            return False

    for y in range(9):
        if su[y][c] == v:
            return False
    
    corner_r = r-r%3   # eg 5%3 will be 2 then 5-2 will give 3 
    corner_c = c-c%3  # 

    for x in range(3):
        for y in range(3):
            if su[corner_r+x][corner_c+y] == v:
                return False
    return True

def try_num(su,r,c):
    if c==9:
        if r == 8:
            return True
        r+=1
        c=0
    if su[r][c] != 0:
        return try_num(su,r,c+1)
    for x in range(1,10):
        if check(su,r,c,x): # if this return true
            su[r][c]=x
            if try_num(su,r,c): # it will check for the next one again and agin at the end it will return and no for for loop will be use any more very clever thing
                return True
        su[r][c] =0
    return False




sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if try_num(sudoku_grid,0,0):
    print("-------Solution exist-----")
    p_su(sudoku_grid)
else:
    print("Solution Don't exist")