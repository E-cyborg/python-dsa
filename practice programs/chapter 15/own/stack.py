class StackOperations:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.pre = None

    def __init__(self):
        self.top = None 

    def push(self, data):
        new_node = self.StackNode(data)
        new_node.pre = self.top
        self.top = new_node

    def display(self):
        def _display(node):
            if node:
                _display(node.pre)
                print(node.data, end=" => ")
        _display(self.top)

    def peek(self):
        if self.top is None:
            print('The stack is empty')
            return None
        return self.top.data
    
    def pop(self):
        if self.top is None:
            print("Stack underflow")
            return None
        tmp = self.top.data
        self.top = self.top.pre
        return tmp
    def isempty(self):
        return self.top==None
        
            