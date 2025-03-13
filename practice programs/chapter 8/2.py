# n-queen 
def is_safe(b, r, c):
    # Check column
    for i in range(r):
        if b[i][c] == "Q":
            return False

    # Check upper-left diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if b[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = r, c
    while i >= 0 and j < len(b):
        if b[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def n_queens(b, r):
    if r == len(b):
        print_board(b)
        print()
        return

    for j in range(len(b)):
        if is_safe(b, r, j):
            b[r][j] = "Q"
            n_queens(b, r + 1)
            b[r][j] = "-"  # Backtrack

def print_board(b):
    for row in b:
        print(" ".join(str(x) for x in row))

# Take user input for board size
n = int(input("Enter nXn board size: "))
board = [["-" for _ in range(n)] for _ in range(n)]
n_queens(board, 0)
