class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j < len(s):
            if s[j] == "#":
                word_length = int(s[i:j])
                res.append(s[j+1:j+1+word_length])
                j = i = j+1+word_length
            else:
                j += 1

        return res
                # "5#Hello5#World"
                #len(s) == 14