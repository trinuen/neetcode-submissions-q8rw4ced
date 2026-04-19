class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in unique:
                count = 0
                while num in unique:
                    num += 1
                    count += 1
                longest = max(longest, count)

        return longest
