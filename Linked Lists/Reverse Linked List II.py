from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head_node: Optional[ListNode]) -> Tuple[ListNode, ListNode]:       
        left_node, middle_node = head_node, head_node.next
        head_node.next = None

        while middle_node:
            right_node = middle_node.next

            middle_node.next = left_node
            left_node = middle_node
            middle_node = right_node

        return left_node, head_node
    
    def reverseBetween(self, head_node: Optional[ListNode], left_index: int, right_index: int) -> Optional[ListNode]:
        if left_index == right_index:
            return head_node

        previous_left, next_left = head_node, head_node
        for _ in range(left_index -1):
            previous_left = next_left
            next_left = next_left.next

        previous_right, next_right = head_node, head_node
        for _ in range(right_index):
            previous_right = next_right
            next_right = next_right.next

        previous_right.next = None
        new_head_node, new_tail_node = self.reverseList(next_left)

        if left_index != 1:
            previous_left.next = new_head_node
        new_tail_node.next = next_right

        return head_node if left_index != 1 else new_head_node   

            
