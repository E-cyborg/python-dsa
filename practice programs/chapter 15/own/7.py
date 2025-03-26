# brackets problem

from stack import StackOperations

def is_balanced(brackets):
    s = StackOperations()
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    for char in brackets:
        if char in bracket_pairs:  
            s.push(char)
        else:  
            if s.isempty() or bracket_pairs[s.pop()] != char:
                return False  
    return s.isempty()


# Test Cases
b = "[{()}]{}"
if is_balanced(b):
    print("Brackets are balanced!")
else:
    print("Brackets are NOT balanced!")