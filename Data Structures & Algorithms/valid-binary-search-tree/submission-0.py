# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, leftb, rightb):
            if not root:
                return True
         
            if root.val > leftb and root.val < rightb:
                leftb = min(leftb, root.val)
                rightb = max(rightb, root.val) 
                return dfs(root.left, leftb, root.val) and dfs(root.right, root.val, rightb)
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))
        

        