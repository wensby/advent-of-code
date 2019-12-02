import importlib
import unittest

solution = importlib.import_module('2019_02_1')

class Test2019Day2Part1(unittest.TestCase):

  def test_example1(self):
    input = '1,9,10,3,2,3,11,0,99,30,40,50,60'
    self.assertEqual(solution.run(input), 3100)
