# stack opertions using queue
from queue import Queue
from stack import StackOperations
def reverse(s):
    q = Queue()
    while not s.isempty():
        q.put(s.pop())
    while not q.empty():
        s.push(q.get())
def reverse_k_element(s,num):
    q=Queue()
    while not s.isempty() and num:
        q.put(s.pop())
        num-=1
    while not q.empty():
        s.push(q.get())

    
s=StackOperations()
s.push(10)
s.push(20)
s.push(30)
s.display()
# reverse(s)
reverse_k_element(s,2)

s.display()