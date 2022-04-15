import io
import sys
import unittest
from custom_list import CustomList


class TestList(unittest.TestCase):
    """Test cases to test CustomList methods"""
    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def test_add(self):
        #смотрим разные тест-кейсы с кастомными листами
        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([6, 3, 10, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([0, 2])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([5, 3, 3, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([0, 2])
        l_2 = CustomList([5, 1, 3, 7])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([5, 3, 3, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([])
        l_2 = CustomList([0, -2])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([0, -2])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        # смотрим разные тест-кейсы с обычными листами справа
        l_1 = CustomList([5, 1, 3, 7])
        l_2 = [1, 2, 7, 0]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([6, 3, 10, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([5, 1, 3, 7])
        l_2 = [1, 2, 7]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([6, 3, 10, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([5, 1, 3])
        l_2 = [1, 2, 7, 0]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([6, 3, 10, 0])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([5, 1, 3])
        l_2 = []
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([5, 1, 3])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([])
        l_2 = [5, 1, 3]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([5, 1, 3])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = CustomList([])
        l_2 = []
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))



        # смотрим разные тест-кейсы с обычными листами слева
        l_1 = [5, 1, 3, 7]
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([6, 3, 10, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = [5, 1, 3, 7]
        l_2 = CustomList([1, 2, 7])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([6, 3, 10, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = [5, 1, 3]
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([6, 3, 10, 0])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = []
        l_2 = CustomList([1, 2, 7])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([1, 2, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = ([1, 2, 7])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([1, 2, 7])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

        l_1 = ([1.0, 2.57, 7.13])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([1.0, 2.57, 7.13])
        self.assertEqual(l_1 + l_2, l_3)
        self.assertTrue(isinstance(l_1 + l_2, CustomList))

    def test_sub(self):
        # смотрим разные тест-кейсы с кастомными листами
        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([1, 2, 7])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([1, 2, 7])
        l_2 = CustomList([5, 1, 3, 7])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([-4, 1, 4, -7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([])
        l_2 = CustomList([5, 1, 3, -7])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([-5, -1, -3, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([5, 1, 3, -7])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([5, 1, 3, -7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        # смотрим разные тест-кейсы с обычными листами справа
        l_1 = CustomList([5, 1, 3, 7])
        l_2 = [1, 2, 7, 0]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([5, 1, 3, 7])
        l_2 = [1, 2, 7]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([5, 1, 3])
        l_2 = [1, 2, 7, 0]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([4, -1, -4, 0])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([5, 1, 3])
        l_2 = []
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([5, 1, 3])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([])
        l_2 = [5, 1, 3]
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([-5, -1, -3])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = CustomList([])
        l_2 = []
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, list))
        l_3 = CustomList([])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        # смотрим разные тест-кейсы с обычными листами слева
        l_1 = [5, 1, 3, 7]
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = [5, 1, 3, 7]
        l_2 = CustomList([1, 2, 7])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([4, -1, -4, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = [5, 1, 3]
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([4, -1, -4, 0])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = []
        l_2 = CustomList([1, 2, 7])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([-1, -2, -7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = ([1, 2, 7])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([1, 2, 7])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

        l_1 = ([1.0, 2.57, 7.13])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, list))
        self.assertTrue(isinstance(l_2, CustomList))
        l_3 = CustomList([1.0, 2.57, 7.13])
        self.assertEqual(l_1 - l_2, l_3)
        self.assertTrue(isinstance(l_1 - l_2, CustomList))

    def test_eq(self):
        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([1, 2, 7, 0])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 != l_2)

        l_1 = CustomList([5, 1, 3, 7])
        l_2 = CustomList([5, 1, 3, 7])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)

        l_1 = CustomList([5, 1, 3, 0])
        l_2 = CustomList([5, 1, 3])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)

        l_1 = CustomList([])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)

        l_1 = CustomList([0, 0, 0, 0, 0])
        l_2 = CustomList([])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)

        l_1 = CustomList([0, 0, 0, 0, 0])
        l_2 = CustomList([1, -1])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)

        l_1 = CustomList([1.0, 2.57, 7.13])
        l_2 = CustomList([1.0, 2.57, 6.13, 1])
        self.assertTrue(isinstance(l_1, CustomList))
        self.assertTrue(isinstance(l_2, CustomList))
        self.assertTrue(l_1 == l_2)


if __name__ == "__main__":
    unittest.main()
