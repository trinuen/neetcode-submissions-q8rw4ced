import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, [dist, point[0], point[1]])
        
        for i in range(k):
            point = heapq.heappop(heap)
            p = [point[1], point[2]]
            res.append(p)
        return res