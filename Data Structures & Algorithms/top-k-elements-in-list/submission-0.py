import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        heap = []

        for num, freq in count.items():
            heap.append((-freq,num))

        heapq.heapify(heap)

        res = []

        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res

        
       