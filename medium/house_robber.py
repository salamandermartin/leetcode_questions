class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        
        
        def robHouse(index):
            if index >= len(nums):
                return 0
            if dp[index] == -1:     #if the max for an index hasnt been calculated yet
                dp[index] = max(robHouse(index + 1), nums[index] + robHouse(index + 2)) ##calculate whether skipping this index will be larger or if taking this index in will be larger
            return dp[index]    #dp[index] will be the largest at the end
        
        
        return robHouse(0)