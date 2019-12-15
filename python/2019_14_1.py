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

  def __repr__(self):
    return f'{self._amount} {self._name}'

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

  def __repr__(self):
    return f'{self._reagents} => {self._result}'

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
    return self._requirements['ORE'].amount

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

def run(input):
  reactions = parse_reactions(input)
  resolver = RequirementResolver(reactions)
  return resolver.solve_for(ChemicalAmount('FUEL', 1))

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
