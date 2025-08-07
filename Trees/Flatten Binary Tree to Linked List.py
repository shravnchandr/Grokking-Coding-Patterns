from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def flatten(self, root_node: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def depth_first_search(current_node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not current_node:
                return current_node
            
            new_left_child = depth_first_search(current_node.left)
            new_right_child = depth_first_search(current_node.right)

            current_node.left = None
            current_node.right = new_left_child

            temp_node = current_node
            while temp_node.right:
                temp_node = temp_node.right

            temp_node.right = new_right_child

            return current_node
        
        depth_first_search(root_node)
