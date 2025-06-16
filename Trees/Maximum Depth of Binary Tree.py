from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root_node: Optional[TreeNode]) -> int:

        def helperFunction(tree_node: Optional[TreeNode], current_depth: int) -> int:
            if not tree_node:
                return current_depth
            
            left_length = helperFunction(tree_node.left, current_depth)
            right_length = helperFunction(tree_node.right, current_depth)

            return 1 + max(left_length, right_length)

        return helperFunction(root_node, 0)        

