class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        #[1,2,4,5]
        #[1,2,2,3,3] limit = 3
        res = 0
        while l <= r:
            # if l == r:
            #     res += 1
            total_weight = people[l] + people[r]
            if total_weight <= limit:
                # res += 1
                l += 1
                # r -= 1
            # else: #total_weight > limit
            res += 1
            r -= 1

        return res