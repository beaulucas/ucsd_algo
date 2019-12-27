#python3
import sys

def get_optimal_value(capacity, values, weights):

  """
  The first line of the input contains the number n of items and the
  capacity W of a knapsack.
  The next n lines define the values and weights of the items.
  The i-th line contains integers v_i and w_i —the value and the weight of i-th item
  :param capacity: total capacity of backpack
  :param weights: list of weights of items
  :param values: list of values of items
  :return:
  """

  # sort list in descending value/weight order
  value_per_weight = [a / b for a, b in zip(values, weights)]
  sorted_items = sorted(zip(value_per_weight, values, weights), reverse=True)
  remaining_item_weight = sum(weights)
  remaining_capacity = capacity
  value = 0

  # keep going if there is space in backpack + items
  while remaining_capacity > 0 and remaining_item_weight > 0:
    for i, v in enumerate(sorted_items):
      # v[0] is value per weight, v[1] is value, v[2] is weight
      if v[2] <= remaining_capacity:
        weight_to_add = v[2]
        value_to_add = v[1]
      else:
        weight_to_add = remaining_capacity
        value_to_add = weight_to_add * v[0]

      remaining_item_weight = remaining_item_weight - weight_to_add
      remaining_capacity = remaining_capacity - weight_to_add
      value = value + value_to_add

  return value

if __name__ == "__main__":
  data = list(map(int, sys.stdin.read().split()))
  n, capacity = data[0:2]
  weights = data[2:(2 * n + 2):2]
  values = data[3:(2 * n + 2):2]
  opt_value = get_optimal_value(capacity, weights, values)
  print("{:.10f}".format(opt_value))