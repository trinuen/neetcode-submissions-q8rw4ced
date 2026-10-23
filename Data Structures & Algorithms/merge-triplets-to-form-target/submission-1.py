class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = triplets[0]
        t0, t1, t2 = target
        for t in triplets:
            if cur[0] > t0 or cur[1] > t1 or cur[2] > t2:
                if t[0] <= t0 or t[1] <= t1 or t[2] <= t2:
                    cur = t
            else:
                if max(cur[0], t[0]) <= t0 and max(cur[1], t[1]) <= t1 and max(cur[2], t[2]) <= t2:
                    cur = [max(cur[0], t[0]), max(cur[1], t[1]), max(cur[2], t[2])]
        
        return cur[0] == target[0] and cur[1] == target[1] and cur[2] == target[2]
        #[10,9,9]