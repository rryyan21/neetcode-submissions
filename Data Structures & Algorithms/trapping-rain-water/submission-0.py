class Solution:
    def trap(self, height: List[int]) -> int:
       leftMax = []
       rightMax = [0] * len(height)
       maxLeft = 0
       maxRight = 0
       maxWater = 0
       
       for i in range(len(height)):
            maxLeft = max(height[i], maxLeft)
            leftMax.append(maxLeft)
            
       for i in range(len(height) - 1, -1, -1):
            maxRight = max(height[i], maxRight)
            rightMax[i] = maxRight

       for i in range(len(height)):
            curr = min(leftMax[i], rightMax[i]) - height[i]
            if curr < 0:
                continue
            maxWater += curr

       return maxWater
        
            
            

            