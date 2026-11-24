# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]
        
    def mergeList(self, l1, l2):
        if l1 and not l2:
            return l1
            
        merged = ListNode(None)
        head = merged
        while l1 and l2:
            if l1.val > l2.val:
                merged.next = l2
                merged = merged.next
                l2 = l2.next
            else:
                merged.next = l1
                merged = merged.next
                l1 = l1.next
        if l1 and not l2:
            merged.next = l1
        elif l2 and not l1:
            merged.next = l2
        return head.next
        
