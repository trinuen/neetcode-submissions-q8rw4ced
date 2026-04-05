class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx = key % 10000
        node = self.map[idx]
        prev = None
        while node:
            if node.key == key:
                node.val = value
                return
            prev = node
            node = node.next

        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % 10000
        node = self.map[idx]

        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % 10000
        node = self.map[idx]

        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                break
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)