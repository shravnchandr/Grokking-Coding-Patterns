from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head_node: Optional[ListNode], target_number: int) -> Optional[ListNode]:
        lesser_than_node, greater_than_node = ListNode(), ListNode()
        less_node, great_node = lesser_than_node, greater_than_node

        traverse_node = head_node
        while traverse_node:
            if traverse_node.val < target_number:
                less_node.next = ListNode(traverse_node.val)
                less_node = less_node.next
            else:
                great_node.next = ListNode(traverse_node.val)
                great_node = great_node.next

            traverse_node = traverse_node.next

        less_node.next = greater_than_node.next
        return lesser_than_node.next

