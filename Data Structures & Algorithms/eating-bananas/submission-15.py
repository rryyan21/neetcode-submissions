class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def canFinish(k):
            total_h = 0

            for i in piles:
                total_h += (i + k - 1) // k

            return total_h <= h



        while low < high:
            mid = (low+high) // 2
            if canFinish(mid):
                high = mid #try to find smaller k 
            else:
                low = mid + 1 #speed is too slow
        return low