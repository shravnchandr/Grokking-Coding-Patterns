from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root_node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root_node:
            return root_node
        
        root_node.left, root_node.right = root_node.right, root_node.left

        self.invertTree(root_node.left)
        self.invertTree(root_node.right)

        return root_node

        def helperFunction(tree_node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not tree_node:
                return
            
            new_right = helperFunction(tree_node.left)
            new_left = helperFunction(tree_node.right)

            tree_node.left, tree_node.right = new_left, new_right
            return tree_node

        return helperFunction(root_node)

        