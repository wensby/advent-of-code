import importlib
import unittest

solver = importlib.import_module('2020_14_2')

class Test2020Day14Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'mask = 000000000000000000000000000000X1001X\n'
        'mem[42] = 100\n'
        'mask = 00000000000000000000000000000000X0XX\n'
        'mem[26] = 1\n'
    )

    self.assertEqual(solver.solve(input), 208)
