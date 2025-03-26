class dll:
    class Node:
        def __init__(self, data, next=None, pre=None):
            self.data = data
            self.next = next
            self.pre = pre            

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertion(self, data):
        self.count += 1
        if self.head is None:  # If the list is empty
            self.head = self.tail = self.Node(data)
            return
        
        new_node = self.Node(data, None, self.tail)  # New node's `pre` is the old tail
        self.tail.next = new_node  # Old tail should point to new node
        self.tail = new_node  # Update tail to the new node

    def insertion_position(self, data, pos):
        if pos > self.count or pos < 0:  # Validate position
            print("Invalid position")
            return 
        
        self.count += 1  # Increase count after validation
        
        if pos == 0:  # Insert at the head
            new_node = self.Node(data, self.head, None) 
            if self.head:
                self.head.pre = new_node  
            else:  # If the list was empty, update tail too
                self.tail = new_node
            self.head = new_node  
            return
        
        tmp = self.head
        for _ in range(pos - 1):  # Traverse to node before the position
            tmp = tmp.next

        new_node = self.Node(data, tmp.next, tmp)  
        
        if tmp.next:  # If not inserting at the end
            tmp.next.pre = new_node
        else:  # If inserting at the end, update tail
            self.tail = new_node
        
        tmp.next = new_node  # Link previous node to new node

    def display(self):
        if self.head is None:
            print('List is empty')
            return
        
        tmp = self.head
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next
        print("None")  # End of list

    def delete_first(self):

        if self.head:
            self.head=self.head.next
            self.tail.pre=self.head
            self.count-=1
        else:
            return
            
    def delete_last(self):
        if self.count == 0:  # If the list is empty, do nothing
            return
        
        self.count -= 1  

        if self.head == self.tail:  # If only one node is present
            self.head = self.tail = None
            return

        tmp = self.tail.pre  # Get the second-last node
        tmp.next = None  # Remove reference to the last node
        self.tail = tmp  # Update tail to second-last node

# **Test the Fixed Code**
do = dll()
do.insertion(1)
do.insertion(12)
do.insertion(3)
do.insertion_position(10, 0)
do.delete_last()
do.display()
