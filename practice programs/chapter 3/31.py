# tri seq

def checking_number(num):
    temp=0
    a=0
    b=1
    c=2
    result= [a,b,c]
    while temp<= num:
        if num in [a,b,c,temp]:
            return True , result
        temp=a+b+c
        a=b
        b=c
        c=temp
        if temp>num:
            return False,result
        result.append(temp)
print('===--- tribonacci series ---===\n\n')
num =input('Ente the number: ')

print(checking_number(int(num)))