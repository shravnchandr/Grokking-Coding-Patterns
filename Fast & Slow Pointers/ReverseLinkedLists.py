from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        if head_node == None or head_node.next == None:
            return head_node

        left_node, middle_node = head_node, head_node.next
        head_node.next = None
        
        while middle_node:
            right_node = middle_node.next
            middle_node.next = left_node

            left_node = middle_node
            middle_node = right_node
                
        return left_node
        