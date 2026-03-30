class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        pre = [1] * n
        suf = [1] * n

        #make prefix
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]

        #make suffix
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]

        for i in range(n):
            res[i] = pre[i] * suf[i]

        return res
        #nums = [1, 2, 4, 6]
        #pre = [1, 1, 2, 8]
        #suf = [48, 24, 6, 1]
        #make res
        