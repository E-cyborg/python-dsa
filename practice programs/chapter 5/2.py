# avg of the given list 
def fun1(lst):
    return sum(lst)/len(lst)

def fun2(lst):
    sum=0
    for i in lst:
        sum +=i
    return sum/len(lst)



print('---| Finding the average of the given list |---')
lst=[]
while True:
    a=input('Enter the numbers:')
    if a == '':
        break
    
    else:
        lst.append(int(a))
        a=None

print('List: ',lst,'\n\n')
print('output of fun1: ',fun1(lst))
print('output of fun2: ',fun2(lst))
