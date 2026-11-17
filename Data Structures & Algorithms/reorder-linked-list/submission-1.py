# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get length / 2
        n = 0
        count = head
        while count:
            n += 1
            count = count.next
        half = n // 2
        length = n

        # go to half point and reverse linked list from that point
        curr = head
        n = half - 1
        i = 0
        while i < n:
            curr = curr.next
            i += 1
        # right now curr = half - 1
        halfpoint = curr.next
        curr.next = None
        prev = None
        current = halfpoint
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # prev has reversed half
        # head has normal half
        # reorder now
        while head.next:
            frontheadnext = head.next
            backheadnext = prev.next

            # point to next values
            head.next = prev
            prev.next = frontheadnext

            # change pointers
            head = frontheadnext
            prev = backheadnext
        
        head.next = prev
        
        
            
            
            
            
            

