from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root_node: Optional[TreeNode], k_index: int) -> int:
        node_count, k_element = 0, None

        def helper_function(tree_node: Optional[TreeNode]) -> None:
            nonlocal node_count, k_element

            if not tree_node or k_element != None:
                return
            
            helper_function(tree_node.left)

            if not k_element:
                node_count = node_count +1

                if node_count == k_index:
                    k_element = tree_node.val
                    return
            
                helper_function(tree_node.right)
            
        helper_function(root_node)
        return k_element


        