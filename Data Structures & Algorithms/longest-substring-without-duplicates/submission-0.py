class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            curr = (r - l) + 1
            longest = max(longest, curr)
            sett.add(s[r])
        
        return longest