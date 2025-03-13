class Tree:
    class Node:
        def __init__(self,data,right=None,left=None):
            self.data  = data
            self.right = right
            self.left  = left
    def __init__(self):
        self.root=None

    def CreateTree(self,l):
        self.root=self.create_tree_util(l,0)
    
    def create_tree_util(self,li,s):
        size=len(li)
        curr=self.Node(li[s])
        l=2*s+1
        r=2*s+2
        if l<size:
            curr.left=self.create_tree_util(li,l)
        if r<size:
            curr.right=self.create_tree_util(li,r)
        return curr
    
    def print_inorder(self):
        self.print_inorder_util(self.root)
        print()

    def print_inorder_util(self,node):
        if node!=None:
            self.print_inorder_util(node.left)
            print(node.data,end="=>")
            self.print_inorder_util(node.right)
    def print_preorder(self):
        self.print_preorder_util(self.root)
        print()
    def print_preorder_util(self,node):
        if node!=None:
            print(node.data,end="=>")
            self.print_preorder_util(node.left)
            self.print_inorder_util(node.right)
    def print_postorder(self):
        self.print_postorder_util(self.root)
    def print_postorder_util(self,node):
        if node!=None:
            self.print_postorder_util(node.left)
            self.print_postorder_util(node.right) 
            print(node.data,end="=>")

    def level_order(self):
        if self.root == None:
            print("Tree is empty")
        q=[]
        q.append(self.root)
        q.append(None)
        while len(q) !=0:
            tmp=q.pop(0)
            if tmp==None:
                print()
                if len(q)==0:
                    break
                else:
                    q.append(None)
            else:
                print(tmp.data,end=" ")
                if tmp.left!=None:
                    q.append(tmp.left)
                if tmp.right!=None:
                    q.append(tmp.right)
    def count_nodes(self,node):
        tmp=node
        if tmp is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    

    def sumofnodes(self, node):
        if node is None:
            return 0  
        return node.data + self.sumofnodes(node.left) + self.sumofnodes(node.right)

    def height_of_tree(self,node):
        # my code
        # tmp=self.root
        # le=0
        # while True:
        #     if tmp==None:
        #         return le
        #     else:
        #         le+=1
        #         tmp=tmp.left
        
        # code from parkah
        if node is None:
            return 0
        hl=self.height_of_tree(node.left)
        hr=self.height_of_tree(node.right)
        return max(hl,hr)+1
    
    def search(self,node,value):
        if node is None:
            return 0
        if node.data==value:
            return True
        if self.search(node.left,value):
            return True
        if self.search(node.right,value):
            return True
        return False
l=[1,2,3,4,5,6,7]
tr=Tree()
tr.CreateTree(l)
# tr.print_inorder()
# tr.print_preorder()
# tr.print_postorder()
# tr.level_order()
# print(tr.sumofnodes(tr.root))
# print(tr.count_nodes(tr.root))
# print(tr.height_of_tree(tr.root))
print(tr.search(tr.root,0))

#  completely understand tree for list

# exiting in 9:55 pm  8-3 25