import importlib
import unittest

solution = importlib.import_module('2020_08_1')

class Test2020Day8Part1(unittest.TestCase):

  def test_example1(self):
    input = (
        'nop +0\n'
        'acc +1\n'
        'jmp +4\n'
        'acc +3\n'
        'jmp -3\n'
        'acc -99\n'
        'acc +1\n'
        'jmp -4\n'
        'acc +6\n'
    )
    self.assertEqual(solution.run(input), 5)
