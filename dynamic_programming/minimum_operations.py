#python3
import sys


def get_min_operations(n):
  """
  Given a calculator that can perform the following operations with `x`,
    * Multiply by 2
    * Multiply by 3
    * Add 1

  Find the minimum number of operations needed to obtain the number {n} starting from the number `1`.
  :param n:
  :return: minimum number of operations needed to obtain {n} starting from `1`
  :return: sequence of potential steps from [1, n]
  """

  def div_two(x):
    return x / 2

  def div_three(x):
    return x / 3

  def minus_one(x):
    return x - 1

  ops = [div_two, div_three, minus_one]
  # starting from 1, see how many operations are required to obtain each step
  # set arbitrary amount n + 1
  min_ops = (n + 1) * [None]
  min_ops[0:2] = [0] * 2

  # generate an efficient previous step for each value n
  last_steps = (n + 1) * [None]

  for n, min_op in enumerate(min_ops):
    # minimizing this value will find most efficient operation to use
    k = len(ops) * [float('Inf')]

    # store possible last values
    back_result = len(ops) * [float('Inf')]
    for i, op in enumerate(ops):
      if n <= 1:
        k[i] = 0
        break
      if type(op(n)) == float and op(n).is_integer() is False:
        pass
      else:
        result = int(op(n))
        # gives the result of applying the operation
        back_result[i] = result
        k[i] = min_ops[result] + 1

    # grab a back result that corresponds with efficient k value
    last_steps[n] = back_result[k.index(min(k))]

    min_ops[n] = min(k)

  sequence = []
  k = n
  # work our way down from n til we hit 1, grabbing an efficient previous step each way
  while k > 1:
    sequence.append(k)
    k = last_steps[k]
  sequence.append(1)
  sequence.reverse()

  return min_ops[n], sequence


if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  m = list(get_min_operations(n))
  sequence = m[1]
  print(m[0])
  for x in sequence:
    print(x, end=' ')
