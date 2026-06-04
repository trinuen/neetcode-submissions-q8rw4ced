class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank = [[] for i in range(len(nums))]
        freq = {}

        #count frequency
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        #{1:1, 2:2, 3:3}
        for key, v in freq.items():
            rank[v-1].append(key)

        res = []
        for i in range(len(rank)-1, -1, -1):
            for num in rank[i]:
                res.append(num)
                if len(res) == k:
                    return res