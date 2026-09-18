class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "_" + word[j+1:]
                nei[pattern].append(word)
        
        res = 1
        q = deque([beginWord])
        visited = set([beginWord])
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord: return res
                for j in range(len(word)):
                    pattern = w[:j] + "_" + w[j+1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0

