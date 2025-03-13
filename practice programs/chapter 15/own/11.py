# eval of prefix
from stack import StackOperations
from infix_to_prefix import infix_prefix

eq = "a+b*c+b"
val = {"a": 10, "b": 20, "c": 30}
exp=['=','+','*','/']
prefix=infix_prefix(eq)
stack=StackOperations()

for x in prefix[::-1]:
    if x  in exp:
        tmp1=stack.pop()
        tmp2=stack.pop()

        op1 = val[tmp1] if tmp1 in val else tmp1
        op2 = val[tmp2] if tmp2 in val else tmp2

        if x=='+':
            result=op1+ op2
        elif x=='-':
            result=op1- op2
        elif x=='*':
            result=op1* op2
        elif x=='/':
            result=op1/ op2
        stack.push(result)
    else:
        stack.push(x)

print(stack.display())
