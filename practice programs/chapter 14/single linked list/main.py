# linked list

# Creation of linked list
class Linked_list:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating the head node
head = Linked_list(10)
print(head.data)  # Output: 10

# Adding a second node
head.next = Linked_list(20)

# Printing the second node's data
print(head.next.data)  # Output: 20
