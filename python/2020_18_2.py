import sys
import operator

func_by_op = {
  '*': operator.mul,
  '+': operator.add
}

def solve(input):
  return sum(evaluate(l) for l in input.splitlines())

def evaluate(expression):
  expression = expression.replace(' ', '')
  if expression.isnumeric():
    return int(expression)
  parts = get_parts(expression)
  if len(parts) == 1:
    return evaluate(parts[0][1:-1])
  for op in ['+', '*']:
    for i, part in enumerate(parts):
      if part == op:
        result = func_by_op[op](evaluate(parts[i-1]), evaluate(parts[i+1]))
        before = ''.join(parts[:i-1])
        after = ''.join(parts[i+2:])
        return evaluate(before+str(result)+after)

  if len(parts) > 1:
    first = evaluate(parts[0])
    second = evaluate(parts[2])
    if parts[1] == '+':
      return evaluate(str(first + second) + ''.join(parts[3:]))
    elif parts[1] == '*':
      return evaluate(str(first * second) + ''.join(parts[3:]))
  else:
    return evaluate(parts[0])

def get_parts(expression):
  part_start = None
  parts = []
  depth = 0
  in_brackets = False
  in_number = False
  for i, c in enumerate(expression):
    if not (in_number or in_brackets):
      if c.isdigit():
        in_number = True
        part_start = i
      elif c == '(':
        depth += 1
        in_brackets = True
        part_start = i
      else:
        parts.append(c)
    elif in_number:
      if c in ['*', '+']:
        in_number = False
        parts.append(expression[part_start:i])
        parts.append(c)
    elif in_brackets:
      if c == '(':
        depth += 1
      elif c == ')':
        depth -= 1
      if depth == 0:
        parts.append(expression[part_start:i+1])
        in_brackets = False
  if in_number:
    parts.append(expression[part_start:i+1])
  return parts

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
