#python3
import sys


def optimal_weight(total_capacity, weights, constraints=True):
  """
  Given `n` gold bars, find the maximum weight of gold that fits into a bag of total {total_capacity}.
  No repetitions, no fractions of bars.
  :param total_capacitycapacity: total capacity of knapsack
  :param weights: weights of the bars of gold
  :param constraints: problem size constraints
  :return: maximum weight of gold that fits into knapsack of {total_capacity}
  """

  if constraints:
    assert total_capacity <= pow(10, 4)
    assert len(weights) <= 300
    assert max(weights) <= pow(10, 5)

  capacities = list(range(0, total_capacity + 1))
  v = [[None] * len(capacities) for i in range(len(weights))]

  for index_weight, weight in enumerate(weights):
    for index_capacity, capacity in enumerate(capacities):
      # base case where we have only one potential item
      if index_weight == 0:
        if weight <= capacity:
          v[index_weight][index_capacity] = weight
        else:
          v[index_weight][index_capacity] = 0
      elif weight > capacity:
        # no ability to use this item, so move up to previous item's subproblem result
        v[index_weight][index_capacity] = v[index_weight - 1][index_capacity]
      elif weight <= capacity:
        # use item, grab weight of previous subproblem, add item weight
        use_value = v[index_weight - 1][index_capacity - weight] + weight
        # dont use, weight doesnt change, weight is equal to subproblem without item
        skip_value = v[index_weight - 1][index_capacity]
        max_value = max(use_value, skip_value)
        v[index_weight][index_capacity] = max_value

  return v[-1][-1]


if __name__ == '__main__':
  input = sys.stdin.read()
  total_capacity, n, *weights = list(map(int, input.split()))
  print(optimal_weight(total_capacity, weights))
