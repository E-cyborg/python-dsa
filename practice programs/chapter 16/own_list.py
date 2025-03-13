
class queue:
    def __init__(self,cap):
        self.que= [None]*cap        # this is a list with none value multiply by cap
        self.cap=cap
        self.count= 0
    
    def empty(self):
        return self.count == 0
    
    def full(self):
        return self.cap==self.count
    
    def size(self):
        return self.count
    
    def display(self):
        print(self.que)
        return 
    def insert(self,data):
        if self.full():
            return 
        self.que[self.count]=data
        self.count+=1
        return

    def pop(self):
        if self.empty():
            return
        self.count-=1
        return self.que.pop(0)

q=queue(5)
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.display()
q.pop()
q.display()