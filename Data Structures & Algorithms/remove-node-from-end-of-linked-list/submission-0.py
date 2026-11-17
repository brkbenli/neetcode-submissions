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
        
        if length == 1:
            return None
        diff = length - n
        print(diff)
        curr = head
        while curr and diff > 1:
            print(curr.val)
            diff -= 1
            curr = curr.next
        curr.next = curr.next.next
        return head
        print(curr.val)