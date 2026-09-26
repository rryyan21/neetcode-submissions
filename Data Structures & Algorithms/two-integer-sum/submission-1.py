class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, val in enumerate(nums):
            remainder = target - val
            if remainder in hashmap:
                return [hashmap[remainder],index]

            hashmap[val] = index

        

        