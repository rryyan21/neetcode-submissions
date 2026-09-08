class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_map = defaultdict(int)
        res = []
        left = 0
        right = 0 

        for right in range(k):
            window_map[nums[right]] += 1

        for right in range(k, len(nums)):
            res.append(max(window_map.keys()))
            window_map[nums[left]] -= 1
            if window_map[nums[left]] == 0:
                del window_map[nums[left]]
            left += 1

            window_map[nums[right]] += 1
        res.append(max(window_map.keys()))
        return res





