# insertion sort

# my code
def insetion_sort(l:list):
    a=len(l)
    for x in range(1,a):
        for y in range(x):
            if l[y]>l[x]:
                l.insert(y,l.pop(x))
    return l





# GPT code 
def insertion_sort1(l: list):
    a = len(l)
    for x in range(1, a):
        key = l[x]
        y = x - 1
        while y >= 0 and l[y] > key:
            l[y + 1] = l[y]  # Shift elements instead of removing/inserting
            y -= 1
        l[y + 1] = key  # Place the key in the correct position
    return l


arr = [3, 1, 2, 2, 5, 4]
list=[1,2,54,6,7,3,2]
print(insetion_sort(arr))
