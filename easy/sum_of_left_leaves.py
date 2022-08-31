# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def sumOfLeftLeaves(self, root: TreeNode):
        if(root == None):
            return 0
        else:
            if(root.left != None and root.left.left == None and root.left.right == None):
                self.sum+= root.left.val
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.sum