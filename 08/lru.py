"""main module"""


class LRUCache:
    """main class"""
    def __init__(self, limit=42):
        if not isinstance(limit, int):
            raise TypeError
        if limit <= 0 or limit >= 10_000:
            raise BufferError
        self.limit = limit
        self.size = 0
        self.cache = []
        self.box = {}

    def get(self, key):
        if key not in self.box:
            return None
        self.cache.remove(key)
        self.cache.append(key)
        return self.box[key]

    def set(self, key, value):
        key.__hash__()  # если ключ не хешируемый, то будет брошено TypeError
        if self.size >= self.limit:
            if key in self.cache:
                self.box[key] = value
                self.cache.remove(key)
                self.cache.append(key)
                return
            self.box.pop(self.cache[0])
            self.cache = self.cache[1:]
            self.cache.append(key)
            self.box[key] = value
        else:
            if key in self.cache:
                self.box[key] = value
                self.cache.remove(key)
                self.cache.append(key)
                return
            self.cache.append(key)
            self.box[key] = value
            self.size += 1
