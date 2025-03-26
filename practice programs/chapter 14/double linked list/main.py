# duble linked list

class dll:
    class Node:
        def __init__(self,data,pre=None,next=None):
            self.pre=pre
            self.data=data
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def size(self):
        return self.count
    def isempty(self):
        return self.count==True
    def printlist(self):
        if self.head== None:
            print("The list is Empty")
            return
        tmp=self.head
        while tmp !=None:
            print(f"{tmp.data}",end="=>")
            tmp=tmp.next
        return 
    
    # printing the list in recursion
    def print_l_recursion(self,tmp):
        if tmp==None:
            print(f"{tmp}",end="")
            return
        print(f"{tmp.data}",end="=>")
        tmp=tmp.next
        self.print_l_recursion(tmp)
        


    def insert_at_first(self,data):
        new_node=self.Node(data,None,None)
        self.count+=1
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            return
        new_node.next=self.head
        self.head.pre = new_node
        self.head=new_node
        return

    def insert_at_last(self,data):
        new_node=self.Node(data,None,None)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.count+=1
            return
        else:
            new_node.pre=self.tail
            self.tail.next=new_node
            self.tail=new_node
            self.count+=1
        return
        
    def __str__(self):
        tmp=self.head
        s="\n"
        while tmp:
            s+=f"{tmp.data}=>"
            tmp=tmp.next
        s+="None"
        return s
        
    def insert_at_specific_loc(self,data,index):
        tmp=self.head
        if 0>index or index>=self.count:
            return None
        if index==0:
            new=self.Node(data,None,self.head)
            self.head.pre=new
            self.head=new
            self.count+1
            return
        index-=1
        while index and tmp:
            tmp=tmp.next
            index-=1
        if tmp==None:
            new=self.Node(data,self.tail,None)
            self.tail.next=new
            self.tail=new
            return
        new=self.Node(data,tmp,tmp.next)
        tmp.next=new
        tmp.next.pre=new
        self.count+=1
        return


    def delete_at_first(self):
        if self.head is None:
            return "the list is empty"

        self.head=self.head.next
        if self.head !=None:
            self.head.pre=None
            self.count-=1
            return
        self.tail=None
        self.count-=1
        return
    
    # delete at last
    def delete_at_last(self):
        if self.tail==None:
            return "The list is empty"
        self.count-=1
        if self.head == self.tail:
            self.head=None
            self.tail=None
            return
        tmp=self.tail.pre
        tmp.next=None
        self.tail=tmp
        return

    def delete_at_specific_loc(self, loc):
        if loc >= self.count or loc<0:  
            return "Error: index out of range"
        
        self.count -= 1  
        if loc == 0:  
            self.delete_at_first()
            return

        tmp = self.head
        tmp2 = None

        while loc: 
            tmp2 = tmp
            tmp = tmp.next
            loc -= 1

        if tmp.next is None:
            tmp2.next = None
            self.tail = tmp2 
            return

        tmp2.next = tmp.next 
        if tmp.next:  
            tmp.next.pre = tmp2  

    def check_list(self,head):
        try:
            tmp=head
            while tmp:
                print(f"pre: {tmp.pre}")
                print(f"data: {tmp.data}")
                print(f"next: {tmp.next}")
                tmp=tmp.next
        except Exception:
            tmp=self.head
            while tmp:
                print(f"pre: {tmp.pre}")
                print(f"data: {tmp.data}")
                print(f"next: {tmp.next}")
                tmp=tmp.next
    def delete_at_specific_element(self,data):
        if self.isempty():
            print("The list is empty")
            return 
        
        tmp=self.head
        tmp2=None
        while tmp.data!=data and tmp:
            tmp2=tmp
            tmp=tmp.next
        if tmp==None:
            print("element not in list")
            return
        if not tmp2:
            self.delete_at_first()
            return
        if tmp.next==None:
            self.delete_at_last()
            return
        self.count-=1
        
        tmp2.next=tmp.next
        tmp.next.pre=tmp2
        return

    def search_element2(self,data):
        if self.isempty():
            print("The list is empty")
            return
        tmp=self.head
        c=0
        while tmp:
            if tmp.data==data:
                print(f"{data} found in location {c}")
                return
            c+=1
            tmp=tmp.next

        if tmp is None:
            print(f"{data} not found")
        return

    def search_element1(self,data):
        if self.isempty():
            print("The list is empty")
            return
        tmp=self.head
        while tmp:
            if tmp.data==data:
                print(f"{data} found")
                return
            tmp=tmp.next

        if tmp is None:
            print(f"{data} not found")
        return
    #easy 
    def copy_list(self):
        if self.isempty():
            print("The list is empty")
            return None

        tmp = self.head
        new_list = dll()  # ✅ Create a new DLL instance

        while tmp:
            new_list.insert_at_last(tmp.data)  # ✅ Insert elements at the last position
            tmp = tmp.next

        return new_list  # ✅ Return the new copied DLL
    # hard
    def copy_list_hard(self):
        if self.isempty():
            print("The list is empty")
            return None  # Fix: Return None instead of printing

        tmp = self.head
        new_list = dll()
        
        # Create first node manually
        new_list.head = new_list.Node(tmp.data, None, None)  
        prev_node = new_list.head  # Track last added node

        tmp = tmp.next  # Move to the next node in the original list

        while tmp:
            new_node = new_list.Node(tmp.data, None, None)  # Create a new node
            prev_node.next = new_node  # Link previous node to new node
            new_node.pre = prev_node  # Link new node back to previous node
            
            prev_node = new_node  # Move prev_node forward
            tmp = tmp.next  # Move tmp forward

        return new_list  # Return the deep-copied DLL

    def rever_list(self):
        if self.isempty():
            return 
        curr=self.head
        pre=None
        while curr:
            pre=curr.pre
            curr.pre=curr.next
            curr.next=pre
            curr=curr.pre
        if pre!=None:
            self.head=self.tail
            
    
list=dll()
list.insert_at_first(400)
list.insert_at_first(300)
list.insert_at_first(200)
print(list)
list.rever_list()
print(list)
