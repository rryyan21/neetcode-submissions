from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq = Counter(tasks)
        cycles = 0
        queue = deque()

        for task, freq in freq.items():
            heap.append((-freq, task))

        heapq.heapify(heap)

        while heap or queue:
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq < 0:    
                    queue.append((freq, task, cycles+n+1))
            
            cycles += 1

            if queue and queue[0][2] <= cycles:
                count, task, ready = queue.popleft()  
                heapq.heappush(heap, (count, task))
            

        return cycles



