import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        heap = []
        res = []

        def dist(x1,y1,x2,y2):
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return distance

        for i in range(n):
            x2,y2 = points[i][0], points[i][1]
            pointDist = dist(0,0,x2,y2)
            heap.append((pointDist, [x2,y2]))

        heapq.heapify(heap)

        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)


        return res






        

