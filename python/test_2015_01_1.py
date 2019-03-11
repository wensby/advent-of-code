import importlib
import unittest

solution = importlib.import_module('2015_01_1')

class Test2015Day1Part1(unittest.TestCase):
  
  def test_example1(self):
    self.assertEqual(solution.run('(())'), 0)

  def test_example2(self):
    self.assertEqual(solution.run('()()'), 0)
  
  def test_example3(self):
    self.assertEqual(solution.run('((('), 3)

  def test_example4(self):
    self.assertEqual(solution.run('(()(()('), 3)

  def test_example5(self):
    self.assertEqual(solution.run('))((((('), 3)

  def test_example6(self):
    self.assertEqual(solution.run('())'), -1)

  def test_example7(self):
    self.assertEqual(solution.run('))('), -1)

  def test_example8(self):
    self.assertEqual(solution.run(')))'), -3)

  def test_example9(self):
    self.assertEqual(solution.run(')())())'), -3)