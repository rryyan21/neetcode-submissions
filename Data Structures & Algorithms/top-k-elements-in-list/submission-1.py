import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        #get frequency 
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        heap = []

        for num, freq in hashmap.items():
            heap.append((-freq,num))

        heapq.heapify(heap)

        res = []

        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res

