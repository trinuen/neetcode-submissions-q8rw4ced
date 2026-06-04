class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest_seq = 0
        for num in nums:
            if num-1 not in unique:
                count = 0
                while num in unique:
                    count += 1
                    num += 1
                longest_seq = max(longest_seq, count)
        return longest_seq