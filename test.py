# from itertools import combinations

# wts = [5, 4, 6, 3]
# w = 10

# # Precompute the values in a dictionary
# w_v = {5: 10, 4: 20, 6: 30, 3: 50}

# # Initialize a variable to track the maximum value
# gr = 0

# # Iterate over the possible combinations
# for r in range(1, len(wts) + 1):
#     for combo in combinations(wts, r):
#         total_weight = sum(combo)
        
#         # Skip combinations that exceed the weight limit
#         if total_weight > w:
#             continue
        
#         # Calculate the total value for the current combination
#         total_value = sum(w_v[item] for item in combo)
        
#         # Update the maximum value if needed
#         if total_value > gr:
#             gr = total_value

# print(gr)


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr  # Base case

#     pivot = arr[len(arr) // 2]  # Choose pivot (middle element)
#     left = [x for x in arr if x < pivot]  # Elements smaller than pivot
#     middle = [x for x in arr if x == pivot]  # Elements equal to pivot
#     right = [x for x in arr if x > pivot]  # Elements greater than pivot

#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage:
# arr = [8, 4, 7, 3, 5, 2, 6]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)  # Output: [2, 3, 4, 5, 6, 7, 8]

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def duplicate_copy(head):
#     if not head:
#         return None  # Handle empty list case

#     new_head = Node(head.data)  # Copy the first node
#     new_tail = new_head
#     current = head.next  # Pointer for traversing original list

#     while current:
#         new_tail.next = Node(current.data)  # Create new node
#         new_tail = new_tail.next  # Move the tail forward
#         current = current.next  # Move in the original list

#     return new_head  # Return the head of the copied list

# # Helper function to print a linked list
# def print_list(head):
#     while head:
#         print(head.data, end=" -> ")
#         head = head.next
#     print("None")

# # Example Usage:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

# print("Original list:")
# print_list(head)

# copied_head = duplicate_copy(head)

# print("Copied list:")
# print_list(copied_head)



brackets={"(":")","[":"]","{":"}"}

