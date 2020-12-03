import importlib
import unittest

solution = importlib.import_module('2020_03_1')

class Test2020Day3Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        '..##.......\n'
        '#...#...#..\n'
        '.#....#..#.\n'
        '..#.#...#.#\n'
        '.#...##..#.\n'
        '..#.##.....\n'
        '.#.#.#....#\n'
        '.#........#\n'
        '#.##...#...\n'
        '#...##....#\n'
        '.#..#...#.#\n'
    )
    self.assertEqual(solution.run(input), 7)
