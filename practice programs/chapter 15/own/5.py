from stack import StackOperations

def BottomInsert(s,data):
    if s.isempty():
        s.push(data)
    else:
        tmp= s.pop()
        BottomInsert(s,data)
        s.push(tmp)

def reverse(s):
    if s.isempty():
        print(None)
        return
    else:
        tmp=s.pop()
        reverse(s)
        BottomInsert(s,tmp)

s=StackOperations()
s.push(10)
BottomInsert(s,20)
BottomInsert(s,20)
BottomInsert(s,20)
reverse(s)
s.display()
