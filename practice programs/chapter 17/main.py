# tree data structure

#                a
#           /       \
#          b        c
#         /  \     /  \
#       e    f    g    h


# it a non liner data structure
# hierarchiacal relationship
# relationship b/w child and parant 
# each node is connect ano'ther node using edges.
# best suitable for search operations

# normal tree vs binary tree
# tree is a finite set of one or more nodes such that 

# 1) there is a specially designed node will be there called root node.
# 2) remaining nodes are partitioned  into n>=0 disjoint set.


# Tree data struct terminologies
# ------------------------------

# root:
#  unique node , having only out going edges


# Fundamental element of a tree, each node has the following three fields 

# 1) data field (actual information) 
# 2) left pointer pointing to left child 
# 3) right pointer pointing to right child 


# edges
# it is use to connect two nodes 
# it is also a fundamenetal part of tree 


# Path
# an order list of nodes that are connect by edges are called as path

# Leaf Nodes
# The node which are not having any children are called as leaf nodes or Nodes without outgoing edges.

# Height of the tree 
# height of the tree summ of edges on the longest path b/w root and leaf node .

# level of tree:
# the level of node/tree is num of edges on the path from root to that node 

# parent
# NOde is parent of all the child that are linked by out going edges.

# children
# Node that are having incoming edges are childrens

# siblings:
# Node in the tree that are children of the same parent are called sibling.

# degree of a node
# total number of sub-trees attached to that node is called as degree of the node.
# aka the number of node are outgoing is a degree

# Degree of tree:
# max Degree of all nodes is called as degree of tree.


# Ancestor:
# A node reachable through repeated moving form child to parent


# Predessor:
# while dispaly/traversing/visiting if node comes before another node it is predessor of that node


# successor:
# while dispaly/traversing/visiting if node comes after another node it is predessor of that node


