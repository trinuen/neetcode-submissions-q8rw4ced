class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        #len(s1) <= len(s2)
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]

        for char in s1:
            freq1[ord(char) - ord('a')] += 1
        print(freq1)

        for i in range(len(s1)):
            freq2[ord(s2[i]) - ord('a')] += 1

        print(freq2)

        if freq1 == freq2: return True

        for i in range(1, len(s2) - len(s1) + 1):
            freq2[ord(s2[i-1]) - ord('a')] -= 1
            freq2[ord(s2[i + len(s1) - 1]) - ord('a')] += 1
            if freq1 == freq2:
                return True

        return False