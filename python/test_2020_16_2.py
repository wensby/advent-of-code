import importlib
import unittest

solver = importlib.import_module('2020_16_2')

class Test2020Day16Part2(unittest.TestCase):

  def test_example1(self):
    input = (
        'class: 0-1 or 4-19\n'
        'row: 0-5 or 8-19\n'
        'seat: 0-13 or 16-19\n'
        '\n'
        'your ticket:\n'
        '11,12,13\n'
        '\n'
        'nearby tickets:\n'
        '3,9,18\n'
        '15,1,5\n'
        '5,14,9\n'
    )

    ticket = solver.solve_your_ticket(input)
    self.assertEqual(ticket['class'], 12)
    self.assertEqual(ticket['row'], 11)
    self.assertEqual(ticket['seat'], 13)
