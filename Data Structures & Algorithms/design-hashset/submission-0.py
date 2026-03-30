class MyHashSet:

    def __init__(self):
        self.keys = []

    def add(self, key: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return None
        self.keys.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                break

    def contains(self, key: int) -> bool:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)