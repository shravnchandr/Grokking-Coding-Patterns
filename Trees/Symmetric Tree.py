from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root_node: Optional[TreeNode]) -> bool:
        
        def helperFunction(root_x: Optional[TreeNode], root_y: Optional[TreeNode]) -> bool:
            if root_x == root_y == None:
                return True
            
            elif None in (root_x, root_y) or root_x.val != root_y.val:
                return False
            
            left_state = helperFunction(root_x.left, root_y.right)
            right_state = helperFunction(root_x.right, root_y.left)
            
            return left_state and right_state
        

        if root_node.left == root_node.right == None:
            return True
        
        elif None in (root_node.left, root_node.right) or root_node.left.val != root_node.right.val:
            return False

        return helperFunction(root_node.left, root_node.right)
    