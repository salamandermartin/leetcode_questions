class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = dict()
        for word in strs:
            if str(sorted(word)) not in hashMap:
                hashMap[str(sorted(word))] = [word]
            else:
                hashMap[str(sorted(word))].append(word)
                
        ans = []
        for i in hashMap:
            ans.append(hashMap[i])
        return ans