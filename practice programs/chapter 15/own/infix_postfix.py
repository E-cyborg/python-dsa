def precedence(x):
    l = {'+': 1, '-': 1, '*': 2, '/': 2}
    return l.get(x, -1)  
def infix_to_postfix(exp):
    s = []
    result = ""
    
    for x in exp:
        if x.isalnum(): 
            result += x
        elif x in ['+', '-', '*', '/']:  
            while s and precedence(x) <= precedence(s[-1]):
                tmp=s.pop()
                result += tmp
            s.append(x)
        elif x == '(': 
            s.append(x)
        elif x == ')':  
            while s and s[-1] != '(':
                tmp=s.pop()
                result += tmp
            s.pop() 
    while s:
        tmp=s.pop() 
        result += tmp
    return result 

# print(f"Infix to Postfix: {infix_to_postfix('(a+b)*c')}")


# steps to convert infix expr into postfix form 
# -----------------------------------------------
# 1) print operands in the same order they arrive. 
# 2) if stack is empty or contains (on top, then push incoming operator 
# 3) if incoming symbol is (then push into stack. 
# 4) if incoming symbol is ) pop all items into output until ( came. 
# 5) if the precedence of incoming symbol is >= precedence of symbol existed in the top of stack, push that symbol into stack. 
# 6) if the precedence of incoming symbol is < precedence of symbol existed in the top of stack, pop the symbol from stack put it into oupt, then compare next symbol. 
# 7) pop all symbols from stack put into output.