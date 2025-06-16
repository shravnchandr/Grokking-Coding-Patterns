from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root_node: 'TreeNode', node_x: 'TreeNode', node_y: 'TreeNode') -> 'TreeNode':
        if node_x.val > node_y.val:
            node_x, node_y = node_y, node_x            
        
        if node_x.val < root_node.val > node_y.val:
            return self.lowestCommonAncestor(root_node.left)
        elif node_x.val > root_node.val < node_y.val:
            return self.lowestCommonAncestor(root_node.right)
        else:
            return root_node
