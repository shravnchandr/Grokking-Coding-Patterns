from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        if head_node == None or head_node.next == None:
            return head_node
        
        left_node, right_node = head_node, head_node.next
        while right_node:
            
            while right_node and left_node.val == right_node.val:
                right_node = right_node.next

            left_node.next = right_node
            left_node = right_node
        
        return head_node
    