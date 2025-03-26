#the O(n^2) quadratic time complexity
def fun(num):
    i=0
    count=0 
    while i<num:
        j=0 
        while j<num:
            k=0
            while k <num:
                count+=1
                k+=1
            j+=1
        i+=1
        
    return count
num=int(input('Enter the number: '))
print(f' {num} the number of instruction in O(n^2) is:' ,fun(num))

#O(n^2)
# number of times loop run = count
# if num = 100
# num^2
# the count will be 10000
