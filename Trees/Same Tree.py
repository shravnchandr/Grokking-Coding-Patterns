from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, root_x: Optional[TreeNode], root_y: Optional[TreeNode]) -> bool:
        if root_x == root_y == None:
            return True
        
        elif None in (root_x, root_y) or root_x.val != root_y.val:
            return False
        
        left_state = self.isSameTree(root_x.left, root_y.left)
        right_state = self.isSameTree(root_x.right, root_y.right)
        
        return left_state and right_state


        