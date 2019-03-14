import importlib
import unittest

solution = importlib.import_module('2015_02_2')

class Test2015Day2Part2(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solution.run('2x3x4'), 34)

  def test_example2(self):
    self.assertEqual(solution.run('1x1x10'), 14)

  def test_multiple_lines(self):
    self.assertEqual(solution.run('2x3x4\n1x1x10'), 48)
