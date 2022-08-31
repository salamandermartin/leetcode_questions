class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midpoint = left + ((right - left) // 2)
            
            if nums[midpoint] == target:
                return midpoint
            
            else:
                if target > nums[midpoint]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
                    
        return -1