from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head_node: 'Optional[Node]') -> 'Optional[Node]':
        if not head_node:
            return None
        
        old_to_new = dict()
        old_to_new[None] = None

        old_node_left, old_node_right = head_node, head_node.next
        new_node_left = Node(x=old_node_left.val)

        while old_node_right:
            new_node_right = Node(old_node_right.val)
            
            new_node_left.next = new_node_right
            old_to_new[old_node_left] = new_node_left

            new_node_left = new_node_right
            old_node_left = old_node_right

            old_node_right = old_node_right.next

        old_to_new[old_node_left] = new_node_left

        old_node = head_node
        while old_node:
            if old_node.random == None:
                old_to_new[old_node].random = None
            else:
                old_to_new[old_node].random = old_to_new[old_node.random]
            
            old_node = old_node.next 

        return old_to_new[head_node]

        