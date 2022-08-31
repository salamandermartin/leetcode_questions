class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node) -> bool:
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:    #if index we're looking for is less than half of the middle we go down left subtree
                node = node.left
                right = pivot
            else:   #if greater than half, we go down right subtree
                node = node.right
                left = pivot + 1
        return node ##checks if a node in the last level exists, they can be labeled from 0 to 2^d - 1
        
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        d = self.compute_depth(root)
        if d == 0:
            return 1
        
        
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return (2**d - 1) + left