import life
import unittest

__author__ = 'Анастасия'


class LifeTest(unittest.TestCase):

    def test_count_neighbors(self):
        a = [
            '.☻.',
            '.☻.',
            '.☻.',
        ]

        self.assertEqual(2, life.count_neighbors(a, 0, 0))
        self.assertEqual(2, life.count_neighbors(a, 1, 1))
        self.assertEqual(1, life.count_neighbors(a, 0, 1))
        self.assertEqual(2, life.count_neighbors(a, 2, 2))
        self.assertEqual(1, life.count_neighbors(a, 2, 1))
        self.assertEqual(3, life.count_neighbors(a, 1, 2))

    def test_tick(self):
        a = [
            '.☻.',
            '.☻.',
            '.☻.',
        ]

        next = [
            list('...'),
            list('☻☻☻'),
            list('...'),
        ]

        b = life.life(a)
        self.assertEqual(next, b)
