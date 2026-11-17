# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        addVal = l1.val + l2.val
        if addVal > 9:
                carry = 1
                addVal = addVal % 10
        addNums = ListNode(addVal)
        head = addNums
        l1 = l1.next
        l2 = l2.next
        
        while l1 and l2:
            addVal = l1.val + l2.val
            addVal += carry
            carry = 0
            if addVal > 9:
                carry = 1
                addVal = addVal % 10
            addNums.next = ListNode(addVal)
            addNums = addNums.next
            l1 = l1.next
            l2 = l2.next
        # now if not equal l1 and l2
        whichIter = None
        if l1 and not l2:
            whichIter = l1
        if l2 and not l1:
            whichIter = l2
        
        while whichIter:
            addVal = whichIter.val + carry
            carry = 0
            if addVal > 9:
                carry = 1
                addVal = addVal % 10
            addNums.next = ListNode(addVal)
            addNums = addNums.next
            whichIter = whichIter.next
        if carry:
            addNums.next = ListNode(carry)
        return head