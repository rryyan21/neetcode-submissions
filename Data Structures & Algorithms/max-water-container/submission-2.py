class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        bestArea = 0

        def calcArea(left, right):
            area = min(heights[left],heights[right]) * (right - left)
            return area
        
        while left < right:
            curr = calcArea(left, right)
            bestArea = max(curr, bestArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return bestArea
            


            