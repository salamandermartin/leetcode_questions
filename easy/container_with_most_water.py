class Solution:
    def maxArea(self, height: List[int]) -> int:
        currArea = 0
        maxArea = 0
        
        l,r = 0, len(height) - 1
        
        while l < r:
            distance = r - l
            curr_height = min(height[l], height[r])
            
            currArea = distance * curr_height
            
            if currArea > maxArea:
                maxArea = currArea
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea
        