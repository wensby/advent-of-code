import importlib
import unittest

solution = importlib.import_module('2019_06_2')

class Test2019Day6Part2(unittest.TestCase):

  def test_example1(self):
    input = (
        'COM)B\n'
        'B)C\n'
        'C)D\n'
        'D)E\n'
        'E)F\n'
        'B)G\n'
        'G)H\n'
        'D)I\n'
        'E)J\n'
        'J)K\n'
        'K)L\n'
        'K)YOU\n'
        'I)SAN\n'
    )
    self.assertEqual(solution.run(input), 4)
