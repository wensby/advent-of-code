import importlib
import unittest

solution = importlib.import_module('2019_14_1')

class Test2019Day14Part1(unittest.TestCase):

  def test_resolve_requirement1(self):
    requirement = solution.ChemicalAmount('FUEL', 1)
    reactions = solution.parse_reactions(
        '1 ORE => 1 FUEL\n'
    )
    solver = solution.RequirementResolver(reactions)
    self.assertEqual(solver.solve_for(requirement), 1)

  def test_resolve_requirement2(self):
    requirement = solution.ChemicalAmount('FUEL', 1)
    reactions = solution.parse_reactions(
        '1 ORE => 2 A\n'
        '1 A => 1 B\n'
        '1 A, 1 B => 1 FUEL\n'
    )
    solver = solution.RequirementResolver(reactions)
    self.assertEqual(solver.solve_for(requirement), 1)

  def test_example1(self):
    string = (
        '10 ORE => 10 A\n'
        '1 ORE => 1 B\n'
        '7 A, 1 B => 1 C\n'
        '7 A, 1 C => 1 D\n'
        '7 A, 1 D => 1 E\n'
        '7 A, 1 E => 1 FUEL\n'
    )
    self.assertEqual(solution.run(string), 31)

  def test_example2(self):
    string = (
        '9 ORE => 2 A\n'
        '8 ORE => 3 B\n'
        '7 ORE => 5 C\n'
        '3 A, 4 B => 1 AB\n'
        '5 B, 7 C => 1 BC\n'
        '4 C, 1 A => 1 CA\n'
        '2 AB, 3 BC, 4 CA => 1 FUEL\n'
    )
    self.assertEqual(solution.run(string), 165)
