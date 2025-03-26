#the O(n) time complexity
def fun(num):
    i=0
    count=0
    while i<num:
        i+=1
        count+=1
    return count
num=int(input('Enter the number: '))
print(f' {num} the number of instruction in O(n) is:' ,fun(num))

# O(n)
# count is representing the number of time the loop run 
# if num = 100
# the time complexity will be 100
