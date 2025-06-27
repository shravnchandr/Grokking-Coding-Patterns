from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head_node: ListNode, reverse_count: int) -> Tuple[ListNode]:
        prev_node, curr_node = None, head_node
        new_tail = head_node

        for _ in range(reverse_count):
            if curr_node is None:
                break

            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        new_head = prev_node
        return new_head, new_tail


    def reverseKGroup(self, head_node: Optional[ListNode], k_index: int) -> Optional[ListNode]:
        if head_node is None or k_index == 1:
            return head_node
        
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
            new_end.next = old_end
            start_node.next = new_start

            start_node = new_end

        return dummy_node.next

            

        