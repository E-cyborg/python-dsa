# # eval post fix


                    # ------------------------ my code -------------------------------
from infix_postfix import *
from stack import StackOperations

eq = "a+b*c+b"
val = {"a": 10, "b": 20, "c": 30}

exp=['=','+','*','/']

res=infix_to_postfix(eq)
stack=StackOperations()
rest=None
for x in res:
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


# ------------------------ end of my code -------------------------------
# Output
# 630