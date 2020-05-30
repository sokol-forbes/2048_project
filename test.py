import unittest
from logics import get_number_from_index, get_empty_list, get_index_from_number, \
    is_zero_in_mas


class Test2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_7(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_8(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_9(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_10(self):
        mas = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11(self):
        mas = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)


if __name__ == 'main':
    unittest.main()