import importlib
import unittest

solution = importlib.import_module('2019_17_1')

class Test2019Day16Part1(unittest.TestCase):

  def test_get_alignment_parameters(self):
    camera_image = (
        '..#..........\n'
        '..#..........\n'
        '#######...###\n'
        '#.#...#...#.#\n'
        '#############\n'
        '..#...#...#..\n'
        '..#####...^..\n'
    )
    alignment_parameteres = solution.get_alignment_parameters(camera_image)
    self.assertEqual(alignment_parameteres, [4, 8, 24, 40])
