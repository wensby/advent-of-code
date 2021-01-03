import importlib
import unittest

solver = importlib.import_module('2020_17_1')

class Test2020Day17Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '.#.\n'
        '..#\n'
        '###\n'
    )
    self.assertEqual(solver.solve(input), 112)
