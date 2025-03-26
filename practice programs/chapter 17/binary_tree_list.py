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
    
    def print_inorder(self,node=None):
        if node:
            self.print_inorder_util(node) 
        else: 
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
    
    def find_maximux(self,node):
        if node is None:
            return float("-inf")
        return max(node.data,self.find_maximux(node.left),self.find_maximux(node.right))
    
    def find_minimum(self,node):
        if node is None:
            return float('inf')
        return min(node.data,self.find_minimum(node.left),self.find_minimum(node.right))

    def LeafNode(self,node):

        if node is None:
            return 0
        if node.right==None and node.left==None:
            return 1
        return self.LeafNode(node.left)+self.LeafNode(node.right)
    def LeafNode_Data(self,node):
        if node is None:
            return 0
        if node.right==None and node.left==None:
            print(node.data)
        return self.LeafNode_Data(node.left)+self.LeafNode_Data(node.right)

    def path(self, node, current_path=""):
        if node is None:
            return
        
        current_path += str(node.data) + " -> "
        
        if node.left is None and node.right is None:
            print(current_path[:-4])  

        self.path(node.left, current_path)
        self.path(node.right, current_path)

    def check_trees(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return self.check_trees(node1.left,node2.left) == self.check_trees(node1.right,node2.right)  and node1.data == node2.data
    # and node1.data == node2.data


    def copy_tree(self):
        return self.copy_tree_util(self.root)

    def copy_tree_util(self, node):
        if node is None:
            return None
        
        # Create a new node with the same data
        new_node = self.Node(node.data)
        
        # Recursively copy left and right subtrees
        new_node.left = self.copy_tree_util(node.left)
        new_node.right = self.copy_tree_util(node.right)
        
        return new_node






l=[1,2,3,4,5,6,100]
tr=Tree()
tr.CreateTree(l)
# tr.print_inorder()
# tr.print_preorder()
# tr.print_postorder()
# tr.level_order()
# print(tr.sumofnodes(tr.root))
# print(tr.count_nodes(tr.root))
# print(tr.height_of_tree(tr.root))
# print(tr.search(tr.root,0))
# print(tr.find_maximux(tr.root))
# print(tr.find_minimum(tr.root))
# print(tr.LeafNode(tr.root))
# print(tr.LeafNode_Data(tr.root))
# print(tr.path(tr.root))
#  completely understand tree for list


# l=[1,2,3,4,5,6,100]
# t=Tree()
# t.CreateTree(l)
# print(tr.check_trees(tr.root,t.root))

new_node = tr.copy_tree()
print(tr.print_inorder(new_node))

# 57 th video complete