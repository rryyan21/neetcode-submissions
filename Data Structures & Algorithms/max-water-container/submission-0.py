class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1   # CHANGE #1
        maxArea = 0

        def calcArea(l, r):        # keep this EXACTLY as is
            width = r - l
            height = min(heights[l], heights[r])
            return width * height

        while left < right:        # correct condition
            currArea = calcArea(left, right)
            maxArea = max(currArea, maxArea)

            # CHANGE #2 – move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1          # move left inward
            else:
                right -= 1         # move right inward

        return maxArea
