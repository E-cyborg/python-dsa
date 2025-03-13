class circular_linked_list:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None  # Ensure next is initialized
    
    def __init__(self):
        self.tail = None
        self.count = 0

    def is_empty(self):
        return "The list is empty" if self.tail is None else self.count

    def display(self):
        if self.tail is None:
            print("The list is empty")
            return

        tmp = self.tail.next
        while True:
            print(tmp.data, end=" => ")
            tmp = tmp.next
            if tmp == self.tail.next: 
                break
        print(None)

    def append_at_first(self, data):
        new_node=self.Node(data)
        if self.tail is None:
            new_node.next=new_node
            self.tail=new_node
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node

    def insert_at_last(self, data):
        new_node = self.Node(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next 
            self.tail.next = new_node 
            self.tail = new_node 
        self.count += 1

    def deletion_atfirst(self):
            if self.tail is None:
                print("The list is already empty")
                return

            if self.tail.next == self.tail:  # If only one node is present
                self.tail = None
            else:
                self.tail.next = self.tail.next.next  # Bypass first node
            
            self.count -= 1  # Decrement count

    def deletion_ending(self):
        tmp=self.tail.next
        pre=None
        if self.tail ==self.tail.next:
            self.tail=None
            return
        if self.tail.next == self.tail:  
            self.tail = None
        else:
            tmp = self.tail.next
            while tmp.next != self.tail:
                tmp = tmp.next
            tmp.next = self.tail.next  
            self.tail = tmp  
        self.count -= 1

        
s = circular_linked_list()
s.append_at_first(10)
s.append_at_first(20)
# s.append_at_first(30)
# s.append_at_first(40)

print("Before Deletion:")
s.display()

s.deletion_atfirst()
print("After Deletion:")
s.display()
s.deletion_ending()
s.display()

