class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        
        def bSearch(arr, target):
            l, r = 0, len(arr) - 1
            
            while l <= r:
                midpoint = l + (r - l // 2)
                
                if arr[midpoint] == target:
                    return True
                
                else:
                    if target > arr[midpoint]:
                        l = midpoint + 1
                    else:
                        r = midpoint - 1
                        
            return False
        
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                return bSearch(matrix[i], target)
                
            i+= 1
                
        return False