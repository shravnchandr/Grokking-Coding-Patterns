from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = dict()
        self.key_queue = deque()

        self.capacity = capacity

    def get(self, key: int) -> int:
        return self.cache_dict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.cache_dict[key] = value
        if key not in self.cache_dict:
            self.key_queue.append(key)

        if len(self.key_queue) > self.capacity:
            del self.cache_dict[self.key_queue.popleft()]

