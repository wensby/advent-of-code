import importlib
import unittest

solver = importlib.import_module('2020_14_1')

class Test2020Day14Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n'
        'mem[8] = 11\n'
        'mem[7] = 101\n'
        'mem[8] = 0\n'
    )

    self.assertEqual(solver.solve(input), 165)
