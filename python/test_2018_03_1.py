import importlib
import unittest

solution = importlib.import_module('2018_03_1')

class Test2018Day3Part1(unittest.TestCase):

  def test_example1(self):
    input = ('#1 @ 1,3: 4x4\n'
             '#2 @ 3,1: 4x4\n'
             '#3 @ 5,5: 2x2\n')
    self.assertEqual(solution.run(input), 4)
