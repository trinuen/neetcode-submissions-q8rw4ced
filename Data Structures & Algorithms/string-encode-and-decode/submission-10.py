class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
        # "512#Hello5#World"

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != '#':
                i += 1
            string_length = int(s[j:i])
            decoded_string.append(s[i+1:i + string_length + 1])
            i = i + string_length + 1
        return decoded_string