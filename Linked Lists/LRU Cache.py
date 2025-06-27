class ListNode:
    def __init__(self, key = 0, value=0, next=None, prev=None):
        self.key, self.value = key, value
        self.next, self.prev = next, prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_capacity = capacity
        self.cache = dict()

        self.lru_node, self.mru_node = ListNode(), ListNode()
        self.lru_node.next, self.mru_node.prev = self.mru_node, self.lru_node

    def insert_node(self, list_node: ListNode) -> None:
        left_node, right_node = self.mru_node.prev, self.mru_node

        left_node.next, right_node.prev = list_node, list_node
        list_node.prev, list_node.next = left_node, right_node

    def remove_node(self, list_node: ListNode) -> None:
        left_node, right_node = list_node.prev, list_node.next
        
        left_node.next, right_node.prev = right_node, left_node

    def get(self, key: int) -> int:
        if key in self.cache:
            key_node = self.cache[key]

            self.remove_node(key_node)
            self.insert_node(key_node)

            return key_node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            key_node = self.cache[key]
            self.remove_node(key_node)

        key_node = ListNode(key, value)
        
        self.cache[key] = key_node
        self.insert_node(key_node)

        if len(self.cache) > self.cache_capacity:
            del_node = self.lru_node.next

            self.remove_node(del_node)
            del self.cache[del_node.value]
