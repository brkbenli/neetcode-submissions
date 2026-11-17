# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checkList = []
        curr = head
        while curr != None:
            checkList.append(curr)
            curr = curr.next
            if curr == None:
                return False
            if curr in checkList:
                return True
        return False