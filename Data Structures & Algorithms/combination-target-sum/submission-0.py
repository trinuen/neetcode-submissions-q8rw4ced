class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = []

        def backtrack(i):
            if sum(total) > target:
                return
            elif sum(total) == target:
                res.append(total[:])
                return
            if i >= len(nums):
                return
            total.append(nums[i])

            backtrack(i)
            total.pop()

            backtrack(i + 1)

        backtrack(0)
        return res
        