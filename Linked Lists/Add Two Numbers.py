from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, list_x: Optional[ListNode], list_y: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        dummy_node = ListNode()
        traverse_node = dummy_node

        node_x, node_y = list_x, list_y
        while node_x and node_y:
            digit = int(node_x.val) + int(node_y.val) + carry
            carry, digit = digit // 10, digit % 10

            traverse_node.next = ListNode(digit)
            traverse_node = traverse_node.next

            node_x, node_y = node_x.next, node_y.next

        while node_x:
            digit = int(node_x.val) + carry
            carry, digit = digit // 10, digit % 10

            traverse_node.next = ListNode(digit)
            traverse_node = traverse_node.next
            node_x = node_x.next

        while node_y:
            digit = int(node_y.val) + carry
            carry, digit = digit // 10, digit % 10

            traverse_node.next = ListNode(digit)
            traverse_node = traverse_node.next
            node_y = node_y.next

        if carry:
            traverse_node.next = ListNode(carry)
            traverse_node = traverse_node.next

        return dummy_node.next
