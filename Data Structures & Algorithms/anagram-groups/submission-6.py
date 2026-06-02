class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #{a: 1, c: 1, t: 1}
        #[]
        #{[1,0,1,0,0,0,0,0..,0]:[act, ]}
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())