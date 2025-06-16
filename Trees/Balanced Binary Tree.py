from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root_node: Optional[TreeNode]) -> bool:
        
        def helperFunction(tree_node: Optional[TreeNode]):
            if not tree_node:
                return 0, True
            
            left_depth, left_balanced = helperFunction(tree_node.left)
            right_depth, right_balanced = helperFunction(tree_node.right)

            is_balanced = (abs(right_depth - left_depth) < 2) and left_balanced and right_balanced

            return 1+ max(left_depth, right_depth), is_balanced
        
        _, root_balanced = helperFunction(root_node)
        return root_balanced


