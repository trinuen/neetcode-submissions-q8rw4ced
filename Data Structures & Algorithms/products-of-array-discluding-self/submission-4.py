class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        #[1,1,1,1]
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(suffix)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        return res