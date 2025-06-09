from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    
    def reorderList(self, head_node: Optional[ListNode]) -> None:
        straight_node, reverse_node = head_node, self.reverseList(head_node)

        temp_node, list_length = head_node, 0
        while temp_node:
            temp_node, list_length = temp_node.next, list_length +1

        middle_count = list_length // 2

        node = head_node
        for _ in range(middle_count):
            node = reverse_node
            straigth_next, reverse_next = straight_node.next, reverse_node.next

            straight_node.next = reverse_node
            reverse_node.next = straigth_next

            straight_node, reverse_node = straigth_next, reverse_next

        if list_length % 2 == 0:
            node.next = None
        else:
            straight_node.next = None

        return head_node
