#  feb seq

def checking_number(num):
    tmp1=0
    a=1
    b=0
    result= []
    while a<= num:
        result.append(b)
        tmp1=a+b
        b=a
        a=tmp1
        if num in [a,b,tmp1]:
            return True , result
    result.append(b)
    return False,result
print('===--- fibonacci series ---===\n\n')
num =input('Ente the number: ')

print(checking_number(int(num)))
