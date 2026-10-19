class Solution:
    def rob(self, nums: List[int]) -> int:
        bestMoneySoFar = 0
        bestFrom2Houses = 0

        for num in nums:
            temp = max(bestMoneySoFar, bestFrom2Houses + num)
            bestFrom2Houses = bestMoneySoFar
            bestMoneySoFar = temp

        
        return bestMoneySoFar

        
            
