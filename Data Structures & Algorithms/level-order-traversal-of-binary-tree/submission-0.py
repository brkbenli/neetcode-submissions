# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if not root:
            return res

        queue.append(root)
        
        while queue:
            qLen = len(queue)
            subList = []
            print(qLen)
            for i in range(qLen):
                x = queue.popleft()
                print(x, x.val)
                print(queue)
                subList.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            print(subList)
            res.append(subList)
            print(res)

        return res