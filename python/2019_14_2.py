import sys
import re
import math

reaction_pattern = re.compile('^(.*) => (.*)$')

class ChemicalAmount:

  def __init__(self, name, amount):
    self._name = name
    self._amount = amount

  @property
  def name(self):
    return self._name

  @property
  def amount(self):
    return self._amount

  def __mul__(self, other):
    return ChemicalAmount(self._name, self._amount * other)

  def __sub__(self, other):
    return ChemicalAmount(self._name, self._amount - other)

  def __add__(self, other):
    return ChemicalAmount(self._name, self._amount + other)

class Reaction:

  def __init__(self, reagents, result):
    self._reagents = reagents
    self._result = result

  @property
  def result(self):
    return self._result

  @property
  def reagents(self):
    return self._reagents

  def __mul__(self, other):
    return Reaction(
        list(map(lambda r: r * other, self._reagents)), 
        self._result * other,
    )

class RequirementResolver:

  def __init__(self, reactions):
    self._reactions = reactions

  def solve_for(self, requirement):
    self._requirements = {requirement.name: requirement}
    while not self._only_ore_positive():
      subject_requirement = self._next_requirement()
      reaction = self._find_reaction(subject_requirement)
      self._requirements[subject_requirement.name] -= reaction.result.amount
      for reagent in reaction.reagents:
        if reagent.name not in self._requirements:
          self._requirements[reagent.name] = ChemicalAmount(reagent.name, 0)
        self._requirements[reagent.name] += reagent.amount
    return self._requirements

  def _positive_requirements(self):
    return [r for r in self._requirements.values() if r.amount > 0]

  def _only_ore_positive(self):
    positive_requirements = self._positive_requirements()
    return len(positive_requirements) == 1 and positive_requirements[0].name == 'ORE'

  def _next_requirement(self):
    for requirement in self._positive_requirements():
      if requirement.name != 'ORE':
        return requirement

  def _find_reaction(self, requirement):
    for reaction in self._reactions:
      if reaction.result.name == requirement.name:
        return reaction

class NanoFactory:

  def __init__(self, reactions):
    self._reactions = reactions

  def produce_fuel(self, chemicals):
    fuel_requirement = self._get_fuel_requirement()
    fuel = 0
    while chemicals['ORE'] >= fuel_requirement['ORE'].amount:
      count = chemicals['ORE'] // fuel_requirement['ORE'].amount
      byproduct = self._get_byproduct_from_producing_fuel(fuel_requirement, count)
      self._add_chemicals(chemicals, byproduct)
      self._distill_chemicals(chemicals)
      fuel += count
    while self._squeeze_out(ChemicalAmount('FUEL', 1), chemicals):
      fuel += 1
    return fuel

  def _get_byproduct_from_producing_fuel(self, fuel_requirement, count):
    return {k: v.amount * -count for k, v in fuel_requirement.items()}

  def _get_fuel_requirement(self):
    resolver = RequirementResolver(self._reactions)
    return resolver.solve_for(ChemicalAmount('FUEL', 1))

  def _add_chemicals(self, chemicals, byproducts):
    for byproduct in byproducts:
      if byproduct not in chemicals:
        chemicals[byproduct] = 0
      chemicals[byproduct] += byproducts[byproduct]

  def _squeeze_out(self, target, available_chemicals):
    if available_chemicals[target.name] >= target.amount:
      available_chemicals[target.name] -= target.amount
      return target.amount
    reaction = self._find_reaction(target.name)
    if not reaction:
      return 0
    missing = target.amount - available_chemicals[target.name]
    reactions_required = math.ceil(missing / reaction.result.amount)
    multiplied_reaction = reaction * reactions_required
    for reagent in multiplied_reaction.reagents:
      if not self._squeeze_out(reagent, available_chemicals):
        return 0
    available_chemicals[target.name] += multiplied_reaction.result.amount
    available_chemicals[target.name] -= target.amount
    return target.amount

  def _find_reaction(self, chemical):
    for reaction in self._reactions:
      if reaction.result.name == chemical:
        return reaction

  def _distill_chemicals(self, chemicals):
    distilled = True
    while distilled:
      distilled = False
      for reaction in self._reactions:
        applied = self.reverse_reaction(reaction, chemicals)
        if applied:
          distilled = True

  def reverse_reaction(self, reaction, chemicals):
    if chemicals[reaction.result.name] >= reaction.result.amount:
      count = chemicals[reaction.result.name] // reaction.result.amount
      modified = reaction * count
      chemicals[reaction.result.name] -= modified.result.amount
      for reagent in modified.reagents:
        chemicals[reagent.name] += reagent.amount
      return True

def run(input):
  reactions = parse_reactions(input)
  factory = NanoFactory(reactions)
  available_chemicals = {'ORE': 1000000000000}
  return factory.produce_fuel(available_chemicals)

def parse_reactions(lines):
  return list(map(parse_reaction, lines.splitlines()))

def parse_reaction(subject):
  match = reaction_pattern.match(subject)
  product = match.group(2).split(' ')
  product_part = ( product[1], int(product[0]) )
  factors = map(lambda x: x.split(' '), match.group(1).split(', '))
  reagents = list(map(lambda r: ChemicalAmount(r[1], int(r[0])), factors))
  result = ChemicalAmount(product[1], int(product[0]))
  return Reaction(reagents, result)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
