class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in hashmap:
                return[hashmap[remainder], i]
            hashmap[n] = i


            