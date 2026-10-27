class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        house1 = nums[0]
        house2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = house2
            house2 = max(house2, nums[i] + house1)
            house1 = temp

        return house2
