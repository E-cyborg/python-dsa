# insertion sorting 


# my code

def fun(l):
    for x in range(1, len(l)): 
        for y in range(0, x): 
            if l[x] < l[y]:
                l.insert(y, l.pop(x)) 
                break 
    print(l)

l = [1, 4, 1, 12, 4, 53, 212]
fun(l)


# code from the course 

def fun(l):
    for x in range(1, len(l)):  # Start from index 1
        key = l[x]  # Element to be placed in sorted part
        y = x - 1   # Compare with previous elements

        while y >= 0 and l[y] > key:  # Shift elements to right if they are greater than key
            l[y + 1] = l[y]
            y -= 1
        
        l[y + 1] = key  # Insert the key at correct position

    print(l)

l = [1, 4, 1, 12, 4, 53, 212]
fun(l)
