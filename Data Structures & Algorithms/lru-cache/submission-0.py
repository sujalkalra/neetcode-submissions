class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapp = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.mapp:
            self.queue.remove(key)
            self.queue.append(key)
            return self.mapp[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.queue.remove(key)
        elif len(self.queue) >= self.capacity:
            lru = self.queue.popleft()
            del self.mapp[lru]
        self.queue.append(key)
        self.mapp[key] = value
