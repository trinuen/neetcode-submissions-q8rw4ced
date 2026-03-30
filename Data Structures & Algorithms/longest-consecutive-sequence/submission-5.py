class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        starts = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                starts.add(num)

        for n in starts:
            seq = 0
            while (n + seq) in nums:
                seq += 1
            longest = max(seq, longest)
        
        return longest
                