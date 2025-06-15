from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, node_x: Optional[ListNode], node_y: Optional[ListNode]) -> Optional[ListNode]:
        if not node_x:
            return node_y
        if not node_y:
            return node_x
        
        merged_node = ListNode(0)
        traverse_node = merged_node

        traverse_node_x, traverse_node_y = node_x, node_y

        while traverse_node_x and traverse_node_y:
            if traverse_node_x.val < traverse_node_y.val:
                traverse_node.next = traverse_node_x
                traverse_node = traverse_node.next

                traverse_node_x = traverse_node_x.next
            else:
                traverse_node.next = traverse_node_y
                traverse_node = traverse_node.next
            
                traverse_node_y = traverse_node_y.next

        if traverse_node_x:
            traverse_node.next = traverse_node_x
        if traverse_node_y:
            traverse_node.next = traverse_node_y

        return merged_node.next