class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        one = 0
        bestLen = 0
        hashset = set()

        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[one])
                one += 1

            hashset.add(s[i])
            bestLen = max(bestLen, i - one + 1)
        
        return bestLen

 
