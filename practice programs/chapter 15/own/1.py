class stack:
    s=[]
    def isempty(self):
        return len(self.s)==0
    def length(self):
        return len(self.s)
    def display(slef):
        for x in slef.s:
            print(x)
        return
    def push(self,data):
        self.s.append(data)
    def poop(self):
        if self.isempty:
            print("list is empty")
            return
        return self.s.pop()
        
    