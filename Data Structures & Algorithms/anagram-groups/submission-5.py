class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #{[]:[""]}
        groups = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord('a') - ord(char)] += 1
            count = tuple(count)
            if count in groups:
                groups[count].append(word)
            else:
                groups[count] = [word]

        res = []

        for key, val in groups.items():
            res.append(val)

        return res