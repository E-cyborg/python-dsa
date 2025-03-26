# steps to convert infix expr into prefix form 
# ---------------------------------------------
# 1) reverse the given expression 
# 2) replace '(' with ')' and '(' with ')' 
# 3) apply infix to postfix conversion 
# 4) reverse generated output 
# infix to prefix conversion implementation

from infix_postfix import *


def infix_prefix(exp):
    exp=list(reversed(exp))

    for x in range(len(exp)):
        if exp[x]=="(":
            exp[x]=")"
        if exp[x]==")":
            exp[x]="("

    postfix=infix_to_postfix(str(exp))
    postfix=postfix[::-1]
    return postfix
    
