class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = i + 1
            j = len(nums)-1
            while k < j:
                threesum = nums[k] + nums[j] + nums[i]
                if threesum > 0:
                    j -= 1
                elif threesum < 0:
                    k += 1
                else:
                    res.append([nums[i], nums[k], nums[j]])
                    k += 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1

        return res