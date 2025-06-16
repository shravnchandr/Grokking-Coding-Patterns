from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root_node: Optional[TreeNode]) -> bool:

        def helperFunction(tree_node: 'TreeNode', min_value: float, max_value: float):
            if tree_node.left == tree_node.right == None:
                return tree_node.val, tree_node.val, min_value < tree_node.val < max_value
            
            if tree_node.left:
                current_min_left, current_max_left, is_valid_left = helperFunction(tree_node.left, min_value, tree_node.val)
                left_ok = current_min_left < tree_node.val > current_max_left
            else:
                current_min_left = current_max_left = tree_node.val
                is_valid_left = left_ok = True

            if tree_node.right:
                current_min_right, current_max_right, is_valid_right = helperFunction(tree_node.right, tree_node.val, max_value)
                right_ok = current_min_right > tree_node.val < current_max_right
            else:
                current_min_right = current_max_right = tree_node.val
                is_valid_right = right_ok = True

            return_min = min(current_min_left, tree_node.val, current_min_right)
            return_max = max(current_max_left, tree_node.val, current_max_right)
            return_ok = is_valid_left and left_ok and is_valid_right and right_ok
            return return_min, return_max, return_ok
        
        _, _, return_ok = helperFunction(root_node, float('-inf'), float('inf'))
        return return_ok



   