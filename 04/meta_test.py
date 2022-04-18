"""main test module"""
import io
import sys
import unittest
from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestMeta(unittest.TestCase):
    """Test cases to test Metaclass"""
    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text


    def test_meta(self):
        """смотрим разные тест-кейсы для мета-класса"""

        # показываем, что немагические атрибуты действительно изменили свои имена на
        # имена с префиксом custom_
        inst = CustomClass()
        self.assertTrue('custom_x' in CustomClass.__dict__)
        self.assertFalse('x' in CustomClass.__dict__)

        self.assertTrue('custom_line' in CustomClass.__dict__)
        self.assertFalse('line' in CustomClass.__dict__)

        # показываем, что магические атрибуты остались неизменными
        self.assertTrue('__str__' in CustomClass.__dict__)
        self.assertFalse('custom___str__' in CustomClass.__dict__)

        self.assertTrue('__init__' in CustomClass.__dict__)
        self.assertFalse('custom___init__' in CustomClass.__dict__)

        # показываем, что изменились только имена немагических атрибутов
        # сами же атрибуты остались неизменными (как магические, так и не магические)

        self.assertEqual(inst.__str__(), "Custom_by_metaclass")
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(inst.custom_x, 50)


if __name__ == "__main__":
    unittest.main()
