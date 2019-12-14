import importlib
import unittest

solution = importlib.import_module('2019_12_2')

class Test2019Day12Part2(unittest.TestCase):

  def test_example_1(self):
    input = (
        '<x=-1, y=0, z=2>\n'
        '<x=2, y=-10, z=-7>\n'
        '<x=4, y=-8, z=8>\n'
        '<x=3, y=5, z=-1>\n'
    )
    self.assertEqual(solution.run(input), 2772)

  def test_example_2(self):
    input = (
        '<x=-8, y=-10, z=0>\n'
        '<x=5, y=5, z=10>\n'
        '<x=2, y=-7, z=3>\n'
        '<x=9, y=-8, z=-3>\n'
    )
    self.assertEqual(solution.run(input), 4686774924)
