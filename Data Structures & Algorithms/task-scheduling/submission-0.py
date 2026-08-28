import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        time = 0
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                if count + 1:
                    q.append([count + 1, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time