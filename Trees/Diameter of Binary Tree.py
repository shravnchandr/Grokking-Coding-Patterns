from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root_node: Optional[TreeNode]) -> int:

        def helperFunction(tree_node: Optional[TreeNode], current_depth: int) -> int:
            if not tree_node:
                return current_depth, 0
            
            left_length, left_max = helperFunction(tree_node.left, current_depth)
            right_length, right_max = helperFunction(tree_node.right, current_depth)

            current_diameter = left_length + right_length
            return 1+ max(left_length, right_length), max(left_max, right_max, current_diameter)

        _, root_max = helperFunction(root_node, 0)
        return root_max

