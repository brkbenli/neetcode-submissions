# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if n == 0:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = None
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        nth = length - n
        if nth == 0:
            return head.next
        if length == 1 and nth == 0:
            return None

        
        i = 0
        prev = head
        while i < nth - 1:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head
        
        
