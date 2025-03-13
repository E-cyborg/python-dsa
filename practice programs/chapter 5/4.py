#genrate a list with odd and even numbers
def fun1(rg):
    o= [x for x in range(0,rg+1,2)]
    e=[x for x in range(1,rg+1,2)]
    return o,e


def fun2(rg):
    o =[x for x in range(0,rg+1) if x%2 == 0]
    e =[x for x in range(0,rg+1) if x%2 != 0]
    return o,e 

def fun3(rg):
    o=[]
    e=[]
    x=0
    while x<= rg:
        if x%2 == 0:
            e.append(x)
        else:
            o.append(x)
        x+=1
    return o,e
def fun4(rg):
    pass



print('===---| odd even number genrator |---===')
rg=int(input('Enter the range:'))


print('List: ',rg,'\n\n')

x,y= fun1(rg)
print(f'output fun1 --: \nodd: {x}  \n\neven: {y}\n\n')

x,y= fun2(rg)
print(f'output fun2 --: \nodd: {x} \n\neven: {y}\n\n')

x,y= fun3(rg)
print(f'output fun3 --: \nodd: {x} \n\neven: {y}')



