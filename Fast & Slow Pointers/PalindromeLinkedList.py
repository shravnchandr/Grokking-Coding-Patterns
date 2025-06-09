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
    
    def isPalindrome(self, head_node: Optional[ListNode]) -> bool:
        temp_node, list_length = head_node, 0
        while temp_node:
            temp_node, list_length = temp_node.next, list_length +1

        middle_count = list_length // 2
        
        temp_node, node = head_node, head_node
        for _ in range(middle_count):
            node = temp_node
            temp_node = temp_node.next        
        node.next = self.reverseList(temp_node)

        left_node, right_node = head_node, node.next
        for _ in range(middle_count):
            if left_node.val != right_node.val:
                return False
            
            left_node, right_node = left_node.next, right_node.next

        return True

