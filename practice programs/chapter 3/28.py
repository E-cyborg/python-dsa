# Armstrong numbers

def fun2(num):
    result=[]
    for i in range(int(num)+1):
        temp=0
        num_l =len(str(i))
        for j in str(i):
            temp+=int(j)**int(num_l)
        if temp == int(i):
            result.append(temp)
    return result





def fun1(num):
    result =0
    l_num =len(num)

    for i in num:
        result+= int(i)**int(l_num)
    if result == int(num):
        return True
    return False

print('--- Armstrong numbers---\n\n')
num =input('Enter the number: ')
print('output of that number: ',fun1(num))
print('output of that number range : ',fun2(num))
