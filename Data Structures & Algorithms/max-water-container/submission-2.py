class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        bestArea = -1
        
        def calcArea(left, right):
            return ((right-left) * (min(heights[left], heights[right])))

        while left < right:
            currArea = calcArea(left, right)
            bestArea = max(bestArea, currArea)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        
        return bestArea
