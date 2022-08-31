class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_anagram = dict()
        t_anagram = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_anagram:
                s_anagram[s[i]] = 1
            elif s[i] in s_anagram:
                s_anagram[s[i]] += 1
            if t[i] not in t_anagram:
                t_anagram[t[i]] = 1
            elif t[i] in t_anagram:
                t_anagram[t[i]] += 1
        return t_anagram == s_anagram