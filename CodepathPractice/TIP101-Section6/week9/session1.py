# S1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# P1 
# def is_symmetric(root):
# 	# recursion
#     if not root:
#         return True
#     # root.left -> root.left.left, root.left.right
#     # root.right -> root.right.left, root.right.right


#     # comparison
#     def is_same(left_number, right_number):
#         #check 
#         if not left_number and not right_number:
#             return True
#         if not left_number or not right_number:
#             return False
        

#         return(left_number.val == right_number.val and 
#                is_same(left_number.left, right_number.right) and
#                is_same(left_number.right, right_number.left)
#                )  
    
#     return is_same(root,root)

    


#     def is_symmetric(root):
#         def is_mirror(l, r):
#             if not l and not r:
#                 return True
#             if not l or not r:
#                 return False
#             if l.val != r.val:
#                 return False

#             left_mirror = is_mirror(l.left, r.right)
#             right_mirror = is_mirror(l.right, r.left)
#             return left_mirror and right_mirror

#     if not root:
#         return True
#     return is_mirror(root.left, root.right)

        
def binary_tree_paths(root):
	#queue
    if not root:
        return []
    
    queue = deque([(root, str(root.val))])
    paths = []

    while queue:
        node, path = queue.popleft()

        if not node.left and not node.right:
            paths.append(path)
        
        if node.left:
            queue.appen((node.left, path + "->" str(node.left.val)))
        if node.right:
            queue.appen((node.right, path + "->" str(node.right.val)))
        
    return paths
        
