class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr_list):
            if len(curr_list) >= len(nums):
                res.append(curr_list.copy())
                return
            for n in nums:
                if n not in curr_list:
                    curr_list.append(n)
                    dfs(curr_list)
                    curr_list.pop()
                
        dfs([])
        return res