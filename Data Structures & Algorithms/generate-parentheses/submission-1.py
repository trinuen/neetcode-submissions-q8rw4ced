class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_count, close_count, p):
            if len(p) >= (2*n):
                res.append(''.join(p))
            if open_count < n:
                p.append("(")
                backtrack(open_count + 1, close_count, p)
                p.pop()
            if close_count < open_count:
                p.append(")")
                backtrack(open_count, close_count + 1, p)
                p.pop()
        backtrack(0, 0, [])
        return res