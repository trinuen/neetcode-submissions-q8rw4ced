import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = [-x for x in stones]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            pop1 = heapq.heappop(stones)
            pop2 = heapq.heappop(stones)
            if pop1 != pop2:
                heapq.heappush(stones, pop1 - pop2)

        if len(stones) == 1:
            return -stones[0]
        return 0
