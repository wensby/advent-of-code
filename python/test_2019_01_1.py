import importlib
import unittest

solution = importlib.import_module('2019_01_1')

class Test2019Day1Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '12\n'
        '14\n'
        '1969\n'
        '100756\n'
    )
    self.assertEqual(solution.run(input), 34241)
