import importlib
import unittest

solution = importlib.import_module('2019_10_1')

class Test2019Day10Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '.#..#\n'
        '.....\n'
        '#####\n'
        '....#\n'
        '...##\n'
    )
    self.assertEqual(solution.run(input), 8)

  def test_example2(self):
    input = (
        '......#.#.\n'
        '#..#.#....\n'
        '..#######.\n'
        '.#.#.###..\n'
        '.#..#.....\n'
        '..#....#.#\n'
        '#..#....#.\n'
        '.##.#..###\n'
        '##...#..#.\n'
        '.#....####\n'
    )
    self.assertEqual(solution.run(input), 33)
