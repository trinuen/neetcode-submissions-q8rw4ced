class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        first_rob1, first_rob2 = nums[0], max(nums[0], nums[1])
        sec_rob1, sec_rob2 = nums[1], max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            temp = first_rob2
            first_rob2 = max(first_rob2, nums[i] + first_rob1)
            first_rob1 = temp

        for i in range(3, len(nums)):
            temp = sec_rob2
            sec_rob2 = max(sec_rob2, nums[i] + sec_rob1)
            sec_rob1 = temp

        return max(first_rob2, sec_rob2)
        