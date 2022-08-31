# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        traversal = []
        
        def bfs(root):
            queue = deque([[root]])
            
            while queue:
                curr = queue.popleft()
                traversal.append(curr)
                
                level = []
                for i in curr:
                    if i:
                        if i.left:
                            level.append(i.left)
                        if i.right:
                            level.append(i.right)
                if level:
                    queue.append(level)
        
        bfs(root)
        ans = []
        for i in traversal:
            ans.append(i[-1].val)
        
        return ans