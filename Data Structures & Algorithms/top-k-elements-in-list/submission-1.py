class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for i in count:
            freq[count[i]].append(i)
        
        res = []
        for c in range(len(freq)-1, 0, -1):
            for i in freq[c]:
                res.append(i)
                if len(res) == k:
                    return res
