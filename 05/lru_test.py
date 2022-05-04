"""main test module"""
import io
import sys
import unittest
from lru import LRUCache


class TestLRU(unittest.TestCase):
    """Test cases to test LRU methods"""
    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def test_different_data_types(self):
        """Test cases to test LRU with different data types"""
        cache = LRUCache()
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k3"), None)
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")

        cache = LRUCache()
        cache.set("k1", 1)
        cache.set("k2", 2)
        self.assertEqual(cache.get("k2"), 2)
        self.assertEqual(cache.get("k1"), 1)
        self.assertEqual(cache.get("k3"), None)
        cache.set("k3", 3)
        self.assertEqual(cache.get("k3"), 3)

        cache = LRUCache()
        cache.set("k1", [1])
        cache.set("k2", [2])
        self.assertEqual(cache.get("k2"), [2])
        self.assertEqual(cache.get("k1"), [1])
        self.assertEqual(cache.get("k3"), None)
        cache.set("k3", [3])
        self.assertEqual(cache.get("k3"), [3])

        cache = LRUCache()
        cache.set("k1", (1, ))
        cache.set("k2", (2, ))
        self.assertEqual(cache.get("k2"), (2,))
        self.assertEqual(cache.get("k1"), (1,))
        self.assertEqual(cache.get("k3"), None)
        cache.set("k3", (3,))
        self.assertEqual(cache.get("k3"), (3,))

    def test_lru_semantics(self):
        """Test cases to test LRU semantics"""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k3"), None)
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")
        # тест set с новым значением по существующему ключу:
        cache.set("k3", "val33")
        self.assertEqual(cache.box["k3"], "val33")
        # покажем, что этот ключ удалится в последнюю очередь:
        cache.set("k4", "val4")
        self.assertTrue("k3" in cache.box)
        self.assertEqual(cache.box["k3"], "val33")
        self.assertFalse("k1" in cache.box)
        cache.set("k5", "val5")
        self.assertFalse("k3" in cache.box)
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k5"), "val5")

    def test_lru_raises(self):
        """Test cases to test LRU raises"""
        with self.assertRaises(BufferError):
            cache = LRUCache(0)

        with self.assertRaises(BufferError):
            cache = LRUCache(-1)

        with self.assertRaises(BufferError):
            cache = LRUCache(10_101)

        with self.assertRaises(TypeError):
            cache = LRUCache('dwvvrwwrvev')

        with self.assertRaises(TypeError):
            cache = LRUCache('')

        with self.assertRaises(TypeError):
            cache = LRUCache('                  ')

        with self.assertRaises(TypeError):
            cache = LRUCache([1, 2])

        cache = LRUCache()
        with self.assertRaises(TypeError):
            cache.set([1], "val")

        with self.assertRaises(TypeError):
            cache.set([], "val")

        with self.assertRaises(TypeError):
            cache.set({}, "val")

        with self.assertRaises(TypeError):
            cache.set({'key': 1}, "val")

        with self.assertRaises(TypeError):
            cache.set({1, 2, 3}, "val")



    def test_different_cases(self):
        """Different test cases"""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k1", "val1_")
        self.assertEqual(cache.get("k1"), "val1_")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k1"), None)

        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k4"), "val4")
        cache.set("k4", [])
        self.assertEqual(cache.get("k4"), [])
        # тест с полным вытеснением элементов
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k4"), "val4")


if __name__ == "__main__":
    unittest.main()
