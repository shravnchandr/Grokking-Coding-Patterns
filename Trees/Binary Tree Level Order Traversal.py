from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root_node: Optional[TreeNode]) -> List[List[int]]:
        level_map = defaultdict(list)
        
        def helperFunction(tree_node: Optional[TreeNode], current_level:int) -> None:
            if not tree_node:
                return
            
            level_map[current_level].append(tree_node.val)
            helperFunction(tree_node.left, current_level +1)
            helperFunction(tree_node.right, current_level +1)

        helperFunction(root_node, 0)
        return list(level_map.values())
    