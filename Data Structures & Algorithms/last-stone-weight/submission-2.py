import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0

        heap = []
        heapq.heapify(heap) #create the heap 
        for i in stones:
                i = i * -1
                heapq.heappush(heap, i)


        while len(heap) > 1:    
            
            heavy1 = heap[0] * -1
            heapq.heappop(heap)
            heavy2 = heap[0] * -1
            heapq.heappop(heap)

            if heavy1 == heavy2:
                continue
            elif heavy2 != heavy1:
                heavy2 = (heavy1 - heavy2) * -1
                heapq.heappush(heap, heavy2)

        if len(heap) == 1:
            return heap[0] *-1
        else:
            return 0 
