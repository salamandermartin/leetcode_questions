class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []
        
        ans = []
        strings = dict()
        l, r = 0, 9
        
        while r < len(s):
            if s[l:r + 1] not in strings:
                strings[s[l:r + 1]] = False
            else:
                if strings[s[l:r+ 1]] == False:
                    ans.append(s[l:r + 1])
                    strings[s[l:r + 1]] = True
            l += 1
            r += 1
        return ans