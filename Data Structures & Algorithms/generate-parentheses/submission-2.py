class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open_count, close_count):
            if open_count > n:
                return
            if len(curr) == 2*n:
                res.append("".join(curr))

            curr.append("(")
            backtrack(curr, open_count+1, close_count)
            curr.pop()
            if open_count > close_count:
                curr.append(")")
                backtrack(curr, open_count, close_count+1)
                curr.pop()
            
        backtrack([], 0, 0)
        return res