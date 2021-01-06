import importlib
import unittest

solver = importlib.import_module('2020_18_1')

class Test2020Day18Part1(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solver.evaluate('1 + 2 * 3 + 4 * 5 + 6'), 71)

  def test_example2(self):
    self.assertEqual(solver.evaluate('1 + (2 * 3) + (4 * (5 + 6))'), 51)

  def test_example3(self):
    self.assertEqual(solver.evaluate('2 * 3 + (4 * 5)'), 26)

  def test_example4(self):
    self.assertEqual(solver.evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)

  def test_example5(self):
    self.assertEqual(solver.evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)

  def test_example6(self):
    self.assertEqual(solver.evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)
