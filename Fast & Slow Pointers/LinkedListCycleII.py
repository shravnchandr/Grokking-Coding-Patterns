from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head_node: Optional[ListNode]) -> bool:
        turtle_node, hare_node = head_node, head_node
        cycle_count = 0
        
        while hare_node and hare_node.next:
            turtle_node, hare_node = turtle_node.next, hare_node.next.next
            cycle_count = cycle_count +1

            if turtle_node == hare_node:
                return cycle_count
                
        return cycle_count -1
    
    def detectCycle(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        cycle_count = self.hasCycle(head_node)

        if cycle_count == -1:
            return None

        turtle_node, hare_node = head_node, head_node
        for _ in range(cycle_count):
            hare_node = hare_node.next

        while turtle_node != hare_node:
            hare_node, turtle_node = hare_node.next, turtle_node.next

        return hare_node
        