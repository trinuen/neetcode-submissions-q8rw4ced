class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 0:
            return 0

        longest = 0
        count = 1
        sorted_list = sorted(nums)
        for i in range(len(nums)-1):
            if (sorted_list[i] + 1 == sorted_list[i + 1]):
                count += 1
            elif (sorted_list[i] == sorted_list[i + 1]):
                continue
            else: 
                if (count > longest):
                    longest = count
                count = 1

        if (count > longest):
            longest = count
        return longest