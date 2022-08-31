class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in values:
                return [i, values[complement]]
            values[nums[i]] = i
            
        
        