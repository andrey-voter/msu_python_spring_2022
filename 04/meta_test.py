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

        # показываем, что имена магических атрибутов остались неизменными
        self.assertTrue('__str__' in CustomClass.__dict__)
        self.assertFalse('custom___str__' in CustomClass.__dict__)

        self.assertTrue('__init__' in CustomClass.__dict__)
        self.assertFalse('custom___init__' in CustomClass.__dict__)

        self.assertTrue('__dict__' in CustomClass.__dict__)
        self.assertFalse('custom___dict__' in CustomClass.__dict__)

        # показываем, что изменились только имена немагических атрибутов
        # сами же атрибуты остались неизменными (как магические, так и не магические)

        self.assertEqual(inst.__str__(), "Custom_by_metaclass")
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(inst.custom_x, 50)

        # показываем, что имена атрибутов, задаваемых как в init так и после init
        # также меняются на имена с префиксом custom_
        self.assertTrue('custom_val' in inst.__dict__)
        self.assertFalse('val' in inst.__dict__)

        inst.field = 22
        self.assertTrue('custom_field' in inst.__dict__)
        self.assertFalse('field' in inst.__dict__)

        self.assertRaises(AttributeError, getattr, inst, 'val')
        self.assertRaises(AttributeError, getattr, inst, 'field')
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_field, 22)

        # еще тесты
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(str(inst), "Custom_by_metaclass")

        self.assertRaises(AttributeError, getattr, inst, 'x')
        self.assertRaises(AttributeError, getattr, inst, 'line')
        self.assertRaises(AttributeError, getattr, CustomClass, 'x')

        # тесты с использованием контекстных менеджеров
        with self.assertRaises(AttributeError):
            inst.line
        with self.assertRaises(AttributeError):
            inst.x
        with self.assertRaises(AttributeError):
            inst.field
        with self.assertRaises(AttributeError):
            inst.val


if __name__ == "__main__":
    unittest.main()
