import importlib
import unittest

solution = importlib.import_module('2019_14_2')

class Test2019Day14Part2(unittest.TestCase):

  def test_example1(self):
    string = (
        '157 ORE => 5 NZVS\n'
        '165 ORE => 6 DCFZ\n'
        '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n'
        '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n'
        '179 ORE => 7 PSHF\n'
        '177 ORE => 5 HKGWZ\n'
        '7 DCFZ, 7 PSHF => 2 XJWVT\n'
        '165 ORE => 2 GPVTF\n'
        '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT\n'
    )
    self.assertEqual(solution.run(string), 82892753)

  def test_example3(self):
    input = (
        '171 ORE => 8 CNZTR\n'
        '7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL\n'
        '114 ORE => 4 BHXH\n'
        '14 VRPVC => 6 BMBT\n'
        '6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL\n'
        '6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT\n'
        '15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW\n'
        '13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW\n'
        '5 BMBT => 4 WPTQ\n'
        '189 ORE => 9 KTJDG\n'
        '1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP\n'
        '12 VRPVC, 27 CNZTR => 2 XDBXC\n'
        '15 KTJDG, 12 BHXH => 5 XCVML\n'
        '3 BHXH, 2 VRPVC => 7 MZWV\n'
        '121 ORE => 7 VRPVC\n'
        '7 XCVML => 6 RJRHP\n'
        '5 BHXH, 4 VRPVC => 5 LTCX\n'
    )
    self.assertEqual(solution.run(input), 460664)
