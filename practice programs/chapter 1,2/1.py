#write a program to take input from the user and conver the even indexing number to upper case

#my code
string=input('Enter the string: ').lower()
a=''
for index,char in enumerate(string):
    if index%2==0:
        a+=string[index].upper()
    else:
        a+=string[index]
print(a)


#sir code
# def fun(string):
#     lst=list(string.lower())
#     for i in range(len(lst)):
#         if i%2==0:
#             lst[i]=lst[i].upper()
#     return ''.join(lst)
# string=input('Enter the string: ')
# print(fun(string))

# chatgpt
# string = input('Enter the string: ')
# result = ''.join([char.upper() if index % 2 == 0 else char for index, char in enumerate(string)])
# print(result)

