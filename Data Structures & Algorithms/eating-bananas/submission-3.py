import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r

        while l <= r:
            total_hours = 0
            mid = (l + r)//2

            for i in piles:
                total_hours += math.ceil(i / mid)

            if total_hours <= h:
                r = mid - 1
                min_rate = min(min_rate, mid)
            else:
                l = mid + 1

        return min_rate