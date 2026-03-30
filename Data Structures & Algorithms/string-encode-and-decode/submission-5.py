class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for text in strs:
            message += str(len(text)) + '#' + text
        return message

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j+=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1])
            i = j + length + 1

        return res

            
