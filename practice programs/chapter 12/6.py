def binary_search(l, k, left, right):
    if left > right:
        return -1  # Element not found

    mid = (left + right) // 2

    if l[mid] == k:
        return mid  # Return index of found element

    if k > l[mid]:
        return binary_search(l, k, mid + 1, right)  # Search right half
    else:
        return binary_search(l, k, left, mid - 1)  # Search left half

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sta=int(input("Enter the staring index: "))
end=int(input("Enter the Ending index: "))
target=int(input("Enter the target value: "))
result = binary_search(arr, target, sta,end)



print(arr)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
