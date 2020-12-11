import importlib
import unittest

solution = importlib.import_module('2020_11_1')

class Test2020Day11Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'L.LL.LL.LL\n'
        'LLLLLLL.LL\n'
        'L.L.L..L..\n'
        'LLLL.LL.LL\n'
        'L.LL.LL.LL\n'
        'L.LLLLL.LL\n'
        '..L.L.....\n'
        'LLLLLLLLLL\n'
        'L.LLLLLL.L\n'
        'L.LLLLL.LL\n'
    )
    self.assertEqual(solution.run(input), 37)
