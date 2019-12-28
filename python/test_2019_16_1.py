import importlib
import unittest

solution = importlib.import_module('2019_16_1')

class Test2019Day16Part1(unittest.TestCase):

  def test_example1(self):
    input_signal = '80871224585914546619083218645595'
    result = solution.run(input_signal)
    self.assertEqual(result, '24176176')

  def test_reverse_fft1(self):
    signal = tuple(range(1, 9))
    self.assertEqual(solution.reverse_fft(signal, 0, 1), 4)
    self.assertEqual(solution.reverse_fft(signal, 1, 1), 8)
    self.assertEqual(solution.reverse_fft(signal, 2, 1), 2)
    self.assertEqual(solution.reverse_fft(signal, 0, 2), 3)
    self.assertEqual(solution.reverse_fft(signal, 0, 3), 0)
    self.assertEqual(solution.reverse_fft(signal, 0, 4), 0)
