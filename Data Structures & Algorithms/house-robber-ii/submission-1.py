class Solution:
    def rob(self, nums: List[int]) -> int:
        prevHouseBest = 0
        prev2Best = 0

        if len(nums) == 1:
            return nums[0]

        for num in nums[:-1]:
            temp = max(prevHouseBest, prev2Best + num)
            prev2Best = prevHouseBest
            prevHouseBest = temp

        res1 = prevHouseBest

        prevHouseBest = 0
        prev2Best = 0

        for num in nums[1:]:
            temp = max(prevHouseBest, prev2Best + num)
            prev2Best = prevHouseBest
            prevHouseBest = temp


        return max(prevHouseBest, res1)
