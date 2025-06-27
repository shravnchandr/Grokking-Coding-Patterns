from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root_node: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def depth_first_search(tree_node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if not tree_node:
                return 0
            
            left_sum = max(0, depth_first_search(tree_node.left))
            right_sum = max(0, depth_first_search(tree_node.right))

            current_sum = left_sum + tree_node.val + right_sum
            max_sum = max(current_sum, max_sum)

            return tree_node.val + max(left_sum, right_sum)
        
        depth_first_search(root_node)
        return max_sum
    