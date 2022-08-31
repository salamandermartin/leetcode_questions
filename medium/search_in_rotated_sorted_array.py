class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            midpoint = (right - left) // 2 + left
            
            if nums[midpoint] == target:
                return midpoint
            
            if nums[left] <= nums[midpoint]:
                if target >= nums[left] and target < nums[midpoint]:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
                    
            else:
                if target < nums[left] and target > nums[midpoint]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1 
                
                
        return -1