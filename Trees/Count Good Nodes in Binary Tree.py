from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root_node: TreeNode) -> int:
        good_nodes_count = 0

        def depth_first_search(tree_node: Optional[TreeNode], current_max: int) -> None:
            nonlocal good_nodes_count

            if not tree_node:
                return

            if tree_node.val >= current_max:
                good_nodes_count = good_nodes_count +1

            depth_first_search(tree_node.left, max(tree_node.val, current_max))
            depth_first_search(tree_node.right, max(tree_node.val, current_max))

        depth_first_search(root_node, root_node.val)
        return good_nodes_count
