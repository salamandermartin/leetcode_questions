class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        
        minimum = float('inf')
        left = 1
            
        while left <= right:
            midpoint = ((right - left) // 2) + left
            eating_time = 0
                
            for pile in piles:
                eating_time += (math.ceil(pile/midpoint))
                    
            if eating_time > h:
                left = midpoint + 1
                
            elif eating_time <= h:
                if midpoint < minimum:
                    minimum = midpoint
                right = midpoint - 1
            
                
        return minimum