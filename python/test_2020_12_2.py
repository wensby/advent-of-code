import importlib
import unittest

solution = importlib.import_module('2020_12_2')

class Test2020Day12Part2(unittest.TestCase):

  def test_example1(self):
    input = (
        'F10\n'
        'N3\n'
        'F7\n'
        'R90\n'
        'F11\n'
    )
    self.assertEqual(solution.run(input), 286)
