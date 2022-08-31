"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def traversal(root):
            queue = deque([[root]])
            
            level = []
            while queue:
                curr = queue.popleft()
                
                value_list = []
                for value in curr:
                    value_list.append(value.val)
                ans.append(value_list)
                
                level = []
                for node in curr:
                    for child in node.children:
                        level.append(child)
                    
                    
                if level:
                    queue.append(level)
                    
        traversal(root)
        return ans