import importlib
import unittest

solution = importlib.import_module('2019_01_2')

class Test2019Day1Part2(unittest.TestCase):

  def test_example1(self):
    input = '14'
    self.assertEqual(solution.run(input), 2)
  
  def test_example2(self):
    input = '1969'
    self.assertEqual(solution.run(input), 966)

  def test_example2(self):
    input = '100756'
    self.assertEqual(solution.run(input), 50346)
