from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root_node: Optional[TreeNode], target_sum: int) -> bool:
        if not root_node:
            return False

        def helperFunction(tree_node: Optional[TreeNode], current_sum: int) -> bool:
            if not tree_node:
                return False
            
            current_sum = current_sum + tree_node.val

            if tree_node.left == tree_node.right == None:
                return current_sum == target_sum

            left_sum = helperFunction(tree_node.left, current_sum)
            right_sum = helperFunction(tree_node.right, current_sum)

            return left_sum or right_sum
        
        return helperFunction(root_node, 0)
            
