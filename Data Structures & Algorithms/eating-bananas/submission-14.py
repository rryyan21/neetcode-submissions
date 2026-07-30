import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        it_works = True
        while left <= right:
            it_works = True
            k = (left + right) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b/k) 
                if hours > h:
                    it_works = False
                    break
            if it_works:
                mink = k
                right = k - 1
            else:
                left = k + 1
        return mink
                

                
                

            
                    






