class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        
        left = 0
        right = 0
        
        ans = []
        
        while right < len(nums):
            while queue and (left > queue[0] or nums[right] > nums[queue[0]]):
                queue.popleft()
                
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
                
            queue.append( right )
            if (right + 1) >= k:
                ans.append(nums[queue[0]])
                left += 1
                
            right += 1
            
                
        return ans