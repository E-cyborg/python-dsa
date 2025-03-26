from collections import deque



# push
stack=deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

# pop

stack.pop()
print(stack)

# check if is empty

print(len(stack)==0)

# len of stack

print(len(stack))