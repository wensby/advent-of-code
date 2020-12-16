import importlib
import unittest

solution = importlib.import_module('2020_13_1')

class Test2020Day13Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '939\n'
        '7,13,x,x,59,x,31,19\n'
    )
    self.assertEqual(solution.run(input), 295)
