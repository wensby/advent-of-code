import importlib
import unittest

solution = importlib.import_module('2019_16_1')

class Test2019Day16Part1(unittest.TestCase):

  def test_example1(self):
    input_signal = '12345678'
    result = solution.fft(input_signal, phases=1)
    self.assertEqual(result, '48226158')

  def test_example2(self):
    input_signal = '12345678'
    result = solution.fft(input_signal, phases=2)
    self.assertEqual(result, '34040438')
  
  def test_example3(self):
    input_signal = '80871224585914546619083218645595'
    result = solution.run(input_signal)
    self.assertEqual(result, '24176176')
