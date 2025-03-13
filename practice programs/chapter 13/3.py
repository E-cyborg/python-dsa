def fun(l, low, high):
    if low >= high:  # Base case
        return

    pivot = l[low]  # Choosing the first element as pivot
    start = low
    end = high

    while low < high:
        while low < high and l[low] <= pivot:
            low += 1
        while low <= high and l[high] > pivot:
            high -= 1

        if low < high:
            l[low], l[high] = l[high], l[low]

    l[start], l[high] = l[high], l[start]  # Place pivot at correct position

    fun(l, start, high - 1)  # Sort left partition
    fun(l, high + 1, end)  # Sort right partition

# Test the function
l = [1, 54, 2, 5, 6532, 3, 5, 35, 2]
print("Before:", l)
fun(l, 0, len(l) - 1)
print("After:", l)








def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    pivot = arr[len(arr) // 2]  # Choose pivot (middle element)
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [8, 4, 7, 3, 5, 2, 6]
print(arr)
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Output: [2, 3, 4, 5, 6, 7, 8]
