# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        res = [root.val]
        if not root:
            return []
        queue = deque()
        queue.append(root)
        
        while queue:
            qLen = len(queue)
            subList = []
            for i in range(qLen):
                x = queue.popleft()
                if x.left:
                    subList.append(x.left.val)
                    queue.append(x.left)
                if x.right:
                    subList.append(x.right.val)
                    queue.append(x.right)
            if subList:
                res.append(subList[-1])
        return res
