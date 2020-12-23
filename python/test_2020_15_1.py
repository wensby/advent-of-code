import importlib
import unittest

solver = importlib.import_module('2020_15_1')

class Test2020Day15Part1(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solver.solve('0,3,6\n'), 436)

  def test_example2(self):
    self.assertEqual(solver.solve('1,3,2\n'), 1)

  def test_example3(self):
    self.assertEqual(solver.solve('2,1,3\n'), 10)

  def test_example4(self):
    self.assertEqual(solver.solve('1,2,3\n'), 27)

  def test_example5(self):
    self.assertEqual(solver.solve('2,3,1\n'), 78)

  def test_example6(self):
    self.assertEqual(solver.solve('3,2,1\n'), 438)

  def test_example7(self):
    self.assertEqual(solver.solve('3,1,2\n'), 1836)
