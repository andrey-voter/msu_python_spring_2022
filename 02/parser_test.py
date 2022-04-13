"""main test module"""
import io
import sys
import unittest
from unittest.mock import patch
from faker import Faker
from my_parser import Parser


def open_f(html, lst):
    lst.append(html)
    return 0


def close_f(html, lst):
    lst.append(html)
    return 0


def data_f(html, lst):
    lst.append(html)
    return 0


class TestParser(unittest.TestCase):
    """Test cases to test Parser methods"""
    def setUp(self):
        self.Parser = Parser(open_f, data_f, close_f)
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def my_clear(self, lst_of_lst, lst1, lst2, lst3):
        lst_of_lst[0].clear()
        lst_of_lst[1].clear()
        lst_of_lst[2].clear()
        lst1.clear()
        lst2.clear()
        lst3.clear()

    def test_parse(self):
        """Test cases to test different input variants"""
        fake = Faker()

        test_string = ""
        container = [[], [], []]
        open_lst = []
        data_lst = []
        close_lst = []
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        test_string = "  "
        container = [[], [], []]
        open_lst = []
        data_lst = ["  ",]
        close_lst = []
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        test_string = "<p>"
        container = [[], [], []]
        open_lst = ['<p>', ]
        data_lst = []
        close_lst = []
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        test_string = "<p></p>"
        open_lst = ['<p>', ]
        data_lst = []
        close_lst = ['</p>', ]
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        text = fake.text(max_nb_chars=20, ext_word_list=None)
        test_string = "<p>" + text + "</p>"
        open_lst = ['<p>', ]
        data_lst = [text]
        close_lst = ['</p>', ]
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        text_1 = fake.text(max_nb_chars=10, ext_word_list=None)
        text_2 = fake.text(max_nb_chars=10, ext_word_list=None)
        text_3 = fake.text(max_nb_chars=10, ext_word_list=None)
        test_string = "<p>" + text_1 + "</p>" + "<meta>" + "<body>"\
                      + text_2 + "<p>" + text_3 + "</p>" + "</body>"
        open_lst = ['<p>', '<meta>', '<body>', '<p>']
        data_lst = [text_1, text_2, text_3]
        close_lst = ['</p>', '</p>', '</body>']
        self.Parser.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

    @patch('parser_test.data_f', return_value=True)
    def test_data_callback(self, mock_data_callback):
        self.assertEqual(mock_data_callback.call_count, 0)
        test_string = "<p>ffffff</p>"
        open_lst = ['<p>', ]
        data_lst = []
        close_lst = ['</p>', ]
        container = [[], [], []]

        # для тестирования с mock
        self.Parser1 = Parser(open_f, data_f, close_f)
        self.Parser1.parse(test_string, container)

        self.assertEqual(mock_data_callback.call_count, 1)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)

        # количество вызовов должно остаться равным 1 (т.к. в тестовой строке только теги)
        test_string = "<p></p>"
        open_lst = ['<p>', ]
        data_lst = []
        close_lst = ['</p>', ]
        self.Parser1.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)
        self.assertEqual(mock_data_callback.call_count, 1)

        # а теперь кол-во вызовов должно стать равным 4
        # (т.к. mock объект должен вызваться три раза
        test_string = "<p>abcd</p><meta content_type><body>my_site_body<p>some_more</p></body>"
        open_lst = ['<p>', '<meta content_type>', '<body>', '<p>']
        data_lst = []
        close_lst = ['</p>', '</p>', '</body>']
        self.Parser1.parse(test_string, container)
        self.assertEqual(container[0], open_lst)
        self.assertEqual(container[1], data_lst)
        self.assertEqual(container[2], close_lst)
        self.my_clear(container, open_lst, data_lst, close_lst)
        self.assertEqual(mock_data_callback.call_count, 4)


if __name__ == "__main__":
    unittest.main()
