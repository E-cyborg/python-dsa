#write a program to take input from the user and conver the odd indexing number to upper case

#my code
string=input('Enter the string: ').lower()
a=''
for index,char in enumerate(string):
    if index%2!=0:
        a+=string[index].upper()
    else:
        a+=string[index]
print(a)
