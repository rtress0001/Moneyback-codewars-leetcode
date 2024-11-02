# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ret = 0
        num_current = head
        
        while num_current:
            ret = (ret << 1) | num_current.val
            num_current = num_current.next
        
        return ret
            