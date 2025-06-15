from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head_node: Optional[ListNode], remove_index: int) -> Optional[ListNode]:
        list_length, traverse_node = 0, head_node
        while traverse_node:
            list_length = list_length +1
            traverse_node = traverse_node.next

        remove_index = list_length - remove_index

        if remove_index == 0:
            return head_node.next

        left_node, right_node = head_node, head_node
        while remove_index > 0:
            left_node = right_node
            right_node = right_node.next
            
            remove_index = remove_index -1

        left_node.next = right_node.next
        return head_node
        

        