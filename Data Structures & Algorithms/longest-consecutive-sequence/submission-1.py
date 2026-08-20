class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0 
        
        for i in nums:
            if i - 1 not in seen: #start of seq 
                count = 1
                while i + 1 in seen:
                    count += 1
                    i += 1

                best = max(count,best)


        return best