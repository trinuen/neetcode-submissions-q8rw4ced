class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(curr_list, i):
            if i >= len(s):
                res.append(curr_list.copy())
                return
            for j in range(i, len(s)):
                sub_string = s[i:j+1]
                if sub_string == sub_string[::-1]:
                    curr_list.append(sub_string)
                    dfs(curr_list, j+1)
                    curr_list.pop()

        dfs([], 0)
        return res