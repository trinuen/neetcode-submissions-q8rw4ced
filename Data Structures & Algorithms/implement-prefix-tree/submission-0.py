class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        root = self.trie

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.is_word = True

    def search(self, word: str) -> bool:
        root = self.trie

        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.is_word

    def startsWith(self, prefix: str) -> bool:
        root = self.trie

        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True
        
        