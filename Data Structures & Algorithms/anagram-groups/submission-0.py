class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        #naive solution
        group = {}
        for i in strs:
            sorted_char = "".join(sorted(i))
            if sorted_char not in group:
                group[sorted_char] = [i]
            else:
                group[sorted_char].append(i)

        res = []
        for i in group:
            res.append(group[i])

        return res