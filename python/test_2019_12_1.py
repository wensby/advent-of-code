import importlib
import unittest

solution = importlib.import_module('2019_12_1')

class Test2019Day12Part1(unittest.TestCase):

  def test_example_1_after_10_steps(self):
    input = (
        '<x=-1, y=0, z=2>\n'
        '<x=2, y=-10, z=-7>\n'
        '<x=4, y=-8, z=8>\n'
        '<x=3, y=5, z=-1>\n'
    )
    moons = solution.parse_moons(input)
    simulation = solution.create_simulation(moons)
    simulation.run(10)
    self.assertEqual(solution.calc_total_energy(moons), 179)

  def test_moon_total_energy(self):
    moon = solution.Moon((2, 1, -3), (-3, -2, 1))
    self.assertEqual(moon.total_energy(), 36)
