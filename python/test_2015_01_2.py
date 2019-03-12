import importlib
import unittest

solution = importlib.import_module('2015_01_2')

class Test2015Day1Part2(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solution.run(')'), 1)

  def test_example2(self):
    self.assertEqual(solution.run('()())'), 5)