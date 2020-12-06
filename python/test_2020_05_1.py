import importlib
import unittest

solution = importlib.import_module('2020_05_1')

class Test2020Day5Part1(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(solution.parse_seat('FBFBBFFRLR'), (44, 5, 357))

  def test_example2(self):
    self.assertEqual(solution.parse_seat('BFFFBBFRRR'), (70, 7, 567))

  def test_example3(self):
    self.assertEqual(solution.parse_seat('FFFBBBFRRR'), (14, 7, 119))

  def test_example4(self):
    self.assertEqual(solution.parse_seat('BBFFBBFRLL'), (102, 4, 820))
