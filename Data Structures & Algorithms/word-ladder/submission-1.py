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
        
        res = 0
        q = deque([beginWord])
        visited = set()
        while q and endWord not in visited:
            for i in range(len(q)):
                w = q.popleft()
                visited.add(w)
                for j in range(len(word)):
                    pattern = w[:j] + "_" + w[j+1:]
                    for n in nei[pattern]:
                        if n != w and n not in visited:
                            q.append(n)
            res += 1
        return res if endWord in visited else 0

