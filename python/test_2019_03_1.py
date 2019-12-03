import importlib
import unittest

solution = importlib.import_module('2019_03_1')

class Test2019Day3Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'R8,U5,L5,D3\n'
        'U7,R6,D4,L4\n'
    )
    self.assertEqual(solution.run(input), 6)

  def test_example2(self):
    input = (
        'R75,D30,R83,U83,L12,D49,R71,U7,L72\n'
        'U62,R66,U55,R34,D71,R55,D58,R83\n'
    )
    self.assertEqual(solution.run(input), 159)

  def test_example3(self):
    input = (
        'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n'
        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7\n'
    )
    self.assertEqual(solution.run(input), 135)
