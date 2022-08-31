class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_length = 0
        longest_string = ''
        
        i = 0
        
        while i < len(s):
            cur_length = 0
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_length = r - l + 1
                cur_string = s[l: r + 1]
                
                l -= 1
                r += 1
                
            if cur_length > longest_length:
                longest_length = cur_length
                longest_string = cur_string
            
            i += 1
        
        i = 0
        while i < len(s) - 1:
            cur_length = 0
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_length = r - l + 1
                cur_string = s[l: r + 1]
                
                l -= 1
                r += 1
                
            if cur_length > longest_length:
                longest_length = cur_length
                longest_string = cur_string
                
            i += 1
            
        return longest_string
            
        
        
        