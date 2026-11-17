# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        nth = length - n - 1
        print(nth)
        if nth <= 0:
            return None
        i = 0
        prev = head
        while i < nth:
            prev = prev.next
            i += 1
        if prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head
