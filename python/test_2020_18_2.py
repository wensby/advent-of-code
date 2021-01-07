import importlib
import unittest

solver = importlib.import_module('2020_18_2')

class Test2020Day18Part2(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solver.evaluate('1 + 2 * 3 + 4 * 5 + 6'), 231)

  def test_example2(self):
    self.assertEqual(solver.evaluate('1 + (2 * 3) + (4 * (5 + 6))'), 51)

  def test_example3(self):
    self.assertEqual(solver.evaluate('2 * 3 + (4 * 5)'), 46)

  def test_example4(self):
    self.assertEqual(solver.evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)

  def test_example5(self):
    self.assertEqual(solver.evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)

  def test_example6(self):
    self.assertEqual(solver.evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)
