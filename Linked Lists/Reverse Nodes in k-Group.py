from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head_node: ListNode, k_index: int) -> Tuple[ListNode]:
        left_node, middle_node = head_node, head_node.next
        head_node.next = None

        for _ in range(k_index):
            right_node = middle_node.next

            middle_node.next = left_node
            left_node = middle_node
            middle_node = right_node

        return left_node, head_node


    def reverseKGroup(self, head_node: Optional[ListNode], k_index: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        start_node, traverse_node = dummy_node, head_node

        while traverse_node:
            index = 1
 
            old_start = traverse_node
            while traverse_node and index < k_index:
                index, traverse_node = index +1, traverse_node.next
            old_end = traverse_node

            traverse_node = traverse_node.next
            if index != k_index:
                break

            new_start, new_end = self.reverse_list(old_start, k_index)
            new_end.next = traverse_node
            start_node.next = new_start

            start_node = new_end

        return dummy_node.next

            

        