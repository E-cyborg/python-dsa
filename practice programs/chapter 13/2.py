def merge_sort(l, i, j):
    if i < j:  # Correct base case
        mid = (i + j) // 2
        merge_sort(l, i, mid)  # Recursively sort left half
        merge_sort(l, mid + 1, j)  # Recursively sort right half
        merge(l, i, mid, j)  # Merge both halves

def merge(l, left, mid, right):
    left_half = l[left:mid + 1]  # Left half includes mid
    right_half = l[mid + 1:right + 1]  # Right half starts at mid+1

    i = j = 0  # Pointers for left and right halves
    k = left  # Pointer for the original list

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            l[k] = left_half[i]
            i += 1
        else:
            l[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        l[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        l[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
l = [1, 5, 2, 5, 3, 6, 53, 2, 7]
print("Original list:", l)
merge_sort(l, 0, len(l) - 1)
print("Sorted list:", l)
