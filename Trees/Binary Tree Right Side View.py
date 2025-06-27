from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root_node: Optional[TreeNode]) -> List[int]:
        if root_node is None:
            return list()
        
        right_view_dict = dict()

        def depth_first_search(tree_node: Optional[TreeNode], current_level: int) -> None:
            if not tree_node:
                return
            
            if current_level not in right_view_dict:
                right_view_dict[current_level] = tree_node.val
            
            depth_first_search(tree_node.right, current_level +1)
            depth_first_search(tree_node.left, current_level +1)


        depth_first_search(root_node, 0)

        right_view_list = list()
        for index in range(len(right_view_dict)):
            right_view_list.append(right_view_dict[index])

        return right_view_list

