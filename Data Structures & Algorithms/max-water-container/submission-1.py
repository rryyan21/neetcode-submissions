class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxArea = 0

        def calcArea(left, right):
            area = (right-left) * min(heights[right], heights[left])

            return area

        
        while left < right:
            curr = calcArea(left, right)
            
            maxArea = max(maxArea, curr)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return maxArea