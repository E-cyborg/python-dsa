class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, n: int):
        self.length = n
        self.count = 0
        self.front = None
        self.rear = None

    def empty(self):
        return self.count == 0

    def full(self):
        return self.count == self.length

    def size(self):
        return self.count

    def display(self):
        tmp = self.front
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next
        print("None")  # To show the end of the queue

    def insert(self, data):
        if self.full():
            print("Queue is full!")
            return
        
        new_node = Node(data)
        
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node  
        self.count += 1

    def pop(self):
        tmp=self.front
        self.front=self.front.next
        if self.front is None:  
             self.rear = None
        self.count-1
        return tmp.data


# Testing
q = Queue(5)
q.display()
q.insert(10)
q.insert(20)
q.insert(30)
q.display()

print("Popped:", q.pop())
q.display()
