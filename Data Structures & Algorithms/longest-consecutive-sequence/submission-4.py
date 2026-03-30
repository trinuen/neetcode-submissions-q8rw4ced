class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = set(nums)
        longest = 0

        for num in nums:
            count = 0
            if (num - 1) not in n:
                while (num + count) in n:
                    count += 1
                longest = max(count, longest)

        return longest
                

        