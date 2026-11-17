"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        seenMap = { None : None}
        curr = head
        # first pass where we clone. dont connect pointers yet
        while curr:
            copy = Node(curr.val)
            seenMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = seenMap[curr]
            copy.next = seenMap[curr.next]
            copy.random = seenMap[curr.random]
            curr = curr.next
        return seenMap[head]
