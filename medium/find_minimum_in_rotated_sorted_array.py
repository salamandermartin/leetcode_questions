class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        currMin = float('inf')
        
        while left <= right:
            midpoint = (right - left) // 2 + left
            
            currMin = min(nums[midpoint], currMin)
            
            if nums[right] > nums[midpoint]:
                right = midpoint - 1
                
            else:
                left = midpoint + 1
                
        return currMin