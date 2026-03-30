import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        l = 1
        r = piles[-1]
        min_rate = piles[-1]

        while l <= r:
            total_hours = 0
            mid = (l + r)//2

            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / mid)

            if total_hours <= h:
                r = mid - 1
                min_rate = min(min_rate, mid)
            else:
                l = mid + 1

        return min_rate