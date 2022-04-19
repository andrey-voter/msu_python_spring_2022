"""main test module"""
import io
import sys
import unittest
from my_descriptors import Data


class TestDescriptors(unittest.TestCase):
    """Test cases to test descriptors"""
    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def test_descriptors(self):
        """смотрим разные тест-кейсы для дескрипторов"""
        data = Data()
        self.assertEqual(data.num, 0)
        self.assertEqual(data.price, 0)
        self.assertEqual(data.name, '')

        data.num = 10
        data.price = 100
        data.name = 'data_name'
        self.assertEqual(data.num, 10)
        self.assertEqual(data.price, 100)
        self.assertEqual(data.name, 'data_name')

        self.assertRaises(ValueError, setattr, data, 'num', 5.54)
        self.assertEqual(data.num, 10)

        self.assertRaises(ValueError, setattr, data, 'price', 18.333)
        self.assertEqual(data.price, 100)

        self.assertRaises(ValueError, setattr, data, 'name', -1)
        self.assertEqual(data.name, 'data_name')

        self.assertRaises(ValueError, setattr, data, 'num', 'abbabab')
        self.assertEqual(data.num, 10)

        self.assertRaises(ValueError, setattr, data, 'price', -1)
        self.assertEqual(data.price, 100)

        self.assertRaises(ValueError, setattr, data, 'name', 188)
        self.assertEqual(data.name, 'data_name')

        self.assertRaises(ValueError, setattr, data, 'num', "")
        self.assertEqual(data.num, 10)

        self.assertRaises(ValueError, setattr, data, 'price', 0)
        self.assertEqual(data.price, 100)

        self.assertRaises(ValueError, setattr, data, 'name', -177.7)
        self.assertEqual(data.name, 'data_name')

        setattr(data, 'num', -25)
        setattr(data, 'price', 200)
        setattr(data, 'name', ' ')
        self.assertEqual(data.num, -25)
        self.assertEqual(data.price, 200)
        self.assertEqual(data.name, ' ')


if __name__ == "__main__":
    unittest.main()
