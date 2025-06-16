from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root_node: Optional[TreeNode]) -> int:
        min_diff, previous_node = float('inf'), None

        def helperFunction(tree_node: Optional[TreeNode]) -> None:
            nonlocal min_diff, previous_node
            
            if not tree_node:
                return
            
            helperFunction(tree_node.left)
            if previous_node:
                min_diff = min(tree_node.val - previous_node.val, min_diff)
            previous_node = tree_node
            helperFunction(tree_node.right)

        helperFunction(root_node)
        return min_diff
