# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, headNode: Optional[ListNode]) -> Optional[ListNode]:
        if headNode == None or headNode.next == None:
            return headNode
        
        leftNode, rightNode = headNode, headNode.next
        while leftNode:

            while rightNode and leftNode.val == rightNode.val:
                rightNode = rightNode.next
            
            leftNode.next= rightNode
            leftNode = rightNode
            # rightNode = rightNode.next
                
        return headNode   


