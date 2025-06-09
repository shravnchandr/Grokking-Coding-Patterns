from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head_node: Optional[ListNode]) -> bool:
        turtle_node, hare_node = head_node, head_node
        
        while hare_node and hare_node.next:
            turtle_node, hare_node = turtle_node.next, hare_node.next.next

            if turtle_node == hare_node:
                return True
                
        return False
        