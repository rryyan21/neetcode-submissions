class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            #check to see if right side is sorted
            if nums[mid] > nums[right]:
                left = mid + 1
            else:              #otherwise its in the left side
                right = mid    #min is at mid or in left

        return nums[left]      #will become mid

