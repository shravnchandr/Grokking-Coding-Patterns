from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        turtle_node, hare_node = head_node, head_node
        
        while hare_node:
            try:
                turtle_node, hare_node = turtle_node.next, hare_node.next.next
            except:
                return turtle_node

        return turtle_node       
        