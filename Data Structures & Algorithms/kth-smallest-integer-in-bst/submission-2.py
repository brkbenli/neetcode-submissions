# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        vals = []
        def dfs(root):
            if not root:
                return None

            vals.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
        dfs(root)
        vals.sort()
        print(vals)
        return vals[k - 1]