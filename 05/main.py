"""example"""
from lru import LRUCache


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.set("k3", "val3")
    print(cache.cache, cache.box)
    cache.set("k3", "val33")
    print(cache.cache, cache.box)
    # print(cache.get("k1"))
    # print(cache.get("k2"))
    # print(cache.get("k3"))


    # print(cache.get("k3"))  # None
    # print(cache.get("k2"))  # "val2"
    # print(cache.get("k1"))  # "val1"
    #
    # cache.set("k3", "val3")
    #
    # print(cache.get("k3"))  # "val3"
    # print(cache.get("k2"))  # None
    # print(cache.get("k1"))  # "val1"
