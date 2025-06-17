import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        big_list = list()

        for index, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(big_list, (linked_list.val, index, linked_list))

        dummy_node = ListNode()
        traverse_node = dummy_node

        while big_list:
            value, index, node = heapq.heappop(big_list)
            traverse_node.next = node
            traverse_node = node
            node = node.next

            if node:
                heapq.heappush(big_list, (node.val, index ,node))

        return dummy_node.next
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        big_list = list()

        for linked_list in lists:
            temp_node = linked_list

            while temp_node:
                big_list.append(temp_node.val)
                temp_node = temp_node.next

        heapq.heapify(big_list)
        
        dummy_node = ListNode()
        traverse_node = dummy_node

        while big_list:
            new_node = ListNode(heapq.heappop(big_list))
            traverse_node.next = new_node
            traverse_node = new_node

        return dummy_node.next
        