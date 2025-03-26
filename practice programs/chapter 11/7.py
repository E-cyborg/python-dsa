# radix sort 

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits (0-9)

    # Count occurrences of each digit at the given place value (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to store the position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing numbers in correct order
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)  # Find the maximum number to determine number of digits
    exp = 1  # Start with the least significant digit (1s place)

    # Apply counting sort for each digit position
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to next digit place (10s, 100s, ...)

# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Before Sorting:", arr)
radix_sort(arr)
print("After Sorting:", arr)
