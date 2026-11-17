# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        if not curr:
            return None
        
        length = 0
        while curr:
            length += 1
            curr = curr.next
        print(length)
        if length == 1:
            return None
        diff = length - n + 1
        

        if length == n:
            return head.next
        curr = head
        x = 1
        while x < n:
            x += 1
            curr = curr.next
        
        print(curr.val)
        curr.next = curr.next.next
        return head
