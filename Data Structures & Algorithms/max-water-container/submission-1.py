class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        bestArea = -1

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            bestArea = max(curr, bestArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return bestArea
            
        