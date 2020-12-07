import importlib
import unittest

solution = importlib.import_module('2020_07_2')

class Test2020Day7Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'light red bags contain 1 bright white bag, 2 muted yellow bags.\n'
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n'
        'bright white bags contain 1 shiny gold bag.\n'
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n'
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n'
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n'
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n'
        'faded blue bags contain no other bags.\n'
        'dotted black bags contain no other bags.\n'
    )
    self.assertEqual(solution.run(input), 32)
