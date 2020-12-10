import importlib
import unittest

solution = importlib.import_module('2020_09_1')

class Test2020Day9Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '35\n'
        '20\n'
        '15\n'
        '25\n'
        '47\n'
        '40\n'
        '62\n'
        '55\n'
        '65\n'
        '95\n'
        '102\n'
        '117\n'
        '150\n'
        '182\n'
        '127\n'
        '219\n'
        '299\n'
        '277\n'
        '309\n'
        '576\n'
    )
    self.assertEqual(solution.solve_with_custom_pool_size(input, 5), 127)
