# 13 -- divide and conquee algo

# divide and conquer is a method , which divides a big problem to samall sub-problems , 
# later we can solve these sub-problems to get the solution for the main problem

# ex: 
#        merge sort 
#        binnery sort 
#        quick sort


# merge sort 



# it only works for if the boh list are sorted only then it can merge in sorted way
def merge_sort(a, b):
    c = []
    a.sort()  # Ensure lists are sorted
    b.sort()
    
    al = len(a)
    bl = len(b)
    i = 0
    j = 0

    while i < al and j < bl:
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1

    while i < al:
        c.append(a[i])
        i += 1  # Fixed increment

    while j < bl:
        c.append(b[j])
        j += 1  # Fixed condition

    print(c)

# Example usage:
a = [1, 4, 2, 3]
b = [5, 7, 3, 6, 2]
print("Original lists:", a, b)
merge_sort(a, b)
