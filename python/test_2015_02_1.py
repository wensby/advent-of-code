import importlib
import unittest

solution = importlib.import_module('2015_02_1')

class Test2015Day2Part1(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solution.run('2x3x4'), 58)

  def test_example2(self):
    self.assertEqual(solution.run('1x1x10'), 43)

  def test_multiple_presents(self):
    input = '2x3x4\n1x1x10'
    self.assertEqual(solution.run(input), 101)
