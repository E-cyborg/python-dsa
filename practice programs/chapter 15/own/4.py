# stack insertion in sorted form

from stack import StackOperations

def sorted_insertion(stk, data):
    if stk.top is None or data >= stk.peek():
        stk.push(data)
        return
    else:
        tmp = stk.pop()
        sorted_insertion(stk, data)
        stk.push(tmp)

def sort_stack(stk):
    if stk.top is not None:
        tmp=stk.pop()
        sort_stack(stk)
        sorted_insertion(stk,tmp)

# Test the code
s = StackOperations()
s.push(4)
s.push(1)
s.push(3)
s.push(2)
# s.pop()
s.display()  # Expected Output: 1 => 3 => 4 => 5 => None

