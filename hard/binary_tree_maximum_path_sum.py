# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(root):
            if root == None:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            self.res = max(self.res, root.val + max(leftMax, 0) + max(rightMax, 0))
            
            return root.val + max(max(leftMax, 0), max(rightMax, 0))
        
        dfs(root)
        return self.res
        