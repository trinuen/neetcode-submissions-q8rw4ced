class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        rank = [[] for i in range(len(nums)+1)]
        freq = {}
        res = []

        #find frequency of each number
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        print(len(rank))
        for j, t in freq.items():
            print(t)
            rank[t].append(j)

        for n in range(len(rank)-1, -1, -1):
            for i in rank[n]:
                res.append(i)
                if len(res) == k:
                    return res
        

