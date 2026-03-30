class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0

        for num in nums:
            if (num - 1) not in nums:
                count = 0
                while num in nums:
                    num +=1
                    count +=1
                longest = max(count, longest)
        return longest