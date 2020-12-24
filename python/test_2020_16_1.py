import importlib
import unittest

solver = importlib.import_module('2020_16_1')

class Test2020Day16Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'class: 1-3 or 5-7\n'
        'row: 6-11 or 33-44\n'
        'seat: 13-40 or 45-50\n'
        '\n'
        'your ticket:\n'
        '7,1,14\n'
        '\n'
        'nearby tickets:\n'
        '7,3,47\n'
        '40,4,50\n'
        '55,2,20\n'
        '38,6,12\n'
    )

    self.assertEqual(solver.solve(input), 71)
