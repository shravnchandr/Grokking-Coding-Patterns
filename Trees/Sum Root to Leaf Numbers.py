from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root_node: Optional[TreeNode]) -> int:

        final_sum = 0
        def depth_first_search(current_node: TreeNode, current_sum: int) -> None:
            nonlocal final_sum

            if not current_node:
                return
            
            current_sum = (current_sum * 10) + current_node.val

            if current_node.left == current_node.right == None:
                final_sum = final_sum + current_sum
                return
            
            depth_first_search(current_node.left, current_sum)
            depth_first_search(current_node.right, current_sum)

        depth_first_search(root_node, 0)
        return final_sum

        